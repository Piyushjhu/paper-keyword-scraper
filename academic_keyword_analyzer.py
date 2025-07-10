#!/usr/bin/env python3

"""
Academic Keyword Analyzer
A legitimate tool for analyzing academic keyword trends using the Semantic Scholar API.

This tool provides comprehensive analysis of academic paper trends by keyword,
using the official Semantic Scholar API (free, no rate limits).

Author: Piyush Wanchoo
GitHub: https://github.com/Piyushjhu
License: MIT
"""

import requests
import time
import json
import sys
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random
import argparse
from pathlib import Path

class AcademicKeywordAnalyzer:
    """
    Main class for analyzing academic keyword trends using Semantic Scholar API.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the Academic Keyword Analyzer
        
        Args:
            api_key (str, optional): Semantic Scholar API key for higher rate limits.
                                   Not required for basic usage.
        """
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.api_key = api_key
        self.headers = {
            'User-Agent': 'AcademicKeywordAnalyzer/1.0'
        }
        if api_key:
            self.headers['x-api-key'] = api_key
    
    def search_papers(self, query, year=None, limit=100, offset=0):
        """
        Search for papers using Semantic Scholar API
        
        Args:
            query (str): Search query
            year (int, optional): Filter by year
            limit (int): Maximum number of results (max 100)
            offset (int): Offset for pagination
            
        Returns:
            dict: API response with papers
        """
        url = f"{self.base_url}/paper/search"
        
        params = {
            'query': query,
            'limit': min(limit, 100),  # API max is 100
            'offset': offset,
            'fields': 'paperId,title,abstract,year,citationCount,referenceCount,venue,publicationDate'
        }
        
        if year:
            params['year'] = year
        
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limited
                print(f"Rate limited by Semantic Scholar API. Waiting 60 seconds...")
                time.sleep(60)
                return None
            else:
                print(f"HTTP Error {e.response.status_code}: {e}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None
    
    def get_paper_count_by_year(self, query, start_year, end_year, verbose=True):
        """
        Get paper count for each year in the range
        
        Args:
            query (str): Search query
            start_year (int): Start year
            end_year (int): End year
            verbose (bool): Print progress messages
            
        Returns:
            list: List of [year, count] pairs
        """
        results = []
        
        for year in range(start_year, end_year + 1):
            if verbose:
                print(f"Searching for papers in {year}...")
            
            # Try up to 3 times for each year
            for attempt in range(3):
                response = self.search_papers(query, year=year, limit=100)
                
                if response and 'total' in response:
                    count = response['total']
                    if verbose:
                        print(f"Found {count:,} papers in {year}")
                    results.append([year, count])
                    break
                elif attempt < 2:  # Not the last attempt
                    if verbose:
                        print(f"Retrying {year} (attempt {attempt + 2}/3)...")
                    time.sleep(5)  # Wait 5 seconds before retry
                else:  # Last attempt failed
                    if verbose:
                        print(f"Could not get results for {year} after 3 attempts")
                    results.append([year, 0])
            
            # Respectful delay between years
            time.sleep(random.uniform(2, 3))
        
        return results
    
    def create_histogram(self, data, search_term, output_filename=None, show_plot=True):
        """
        Create a histogram from the data
        
        Args:
            data (list): List of [year, count] pairs
            search_term (str): Search term for title
            output_filename (str, optional): Output filename
            show_plot (bool): Whether to display the plot
        """
        years = [row[0] for row in data]
        counts = [row[1] for row in data]
        
        # Set up matplotlib
        plt.figure(figsize=(12, 8))
        
        # Create bar chart
        bars = plt.bar(years, counts, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
        
        # Add value labels on top of bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + max(counts)*0.01,
                    f'{count:,}', ha='center', va='bottom', fontsize=10)
        
        # Customize the plot
        plt.title(f'Semantic Scholar Results for "{search_term}" by Year', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Academic Papers', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.xticks(years, rotation=45)
        plt.tight_layout()
        
        # Save the plot if filename provided
        if output_filename:
            plt.savefig(output_filename, dpi=300, bbox_inches='tight')
            print(f"Histogram saved as {output_filename}")
        
        # Show the plot if requested
        if show_plot:
            plt.show()
        else:
            plt.close()
    
    def save_to_csv(self, data, filename):
        """
        Save results to CSV file
        
        Args:
            data (list): List of [year, count] pairs
            filename (str): Output filename
        """
        df = pd.DataFrame(data, columns=['year', 'paper_count'])
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
    
    def analyze_keyword(self, search_term, start_year, end_year, output_dir=".", 
                       generate_chart=True, show_plot=True, verbose=True):
        """
        Complete analysis workflow
        
        Args:
            search_term (str): Search term
            start_year (int): Start year
            end_year (int): End year
            output_dir (str): Output directory
            generate_chart (bool): Generate histogram
            show_plot (bool): Show plot interactively
            verbose (bool): Print progress messages
            
        Returns:
            dict: Analysis results
        """
        if verbose:
            print(f"Analyzing '{search_term}' from {start_year} to {end_year}")
            print("=" * 60)
        
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Get data
        results = self.get_paper_count_by_year(search_term, start_year, end_year, verbose)
        
        # Create safe filename
        safe_search_term = "".join(c for c in search_term if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_search_term = safe_search_term.replace(' ', '_')
        
        # Save to CSV
        csv_filename = Path(output_dir) / f"{safe_search_term}_{start_year}_{end_year}_results.csv"
        self.save_to_csv(results, csv_filename)
        
        # Generate chart if requested
        chart_filename = None
        if generate_chart and results:
            chart_filename = Path(output_dir) / f"{safe_search_term}_{start_year}_{end_year}_histogram.png"
            self.create_histogram(results, search_term, chart_filename, show_plot)
        
        # Calculate summary statistics
        total_papers = sum(row[1] for row in results)
        avg_papers = total_papers / len(results) if results else 0
        max_year = max(results, key=lambda x: x[1]) if results else None
        
        summary = {
            'search_term': search_term,
            'start_year': start_year,
            'end_year': end_year,
            'total_papers': total_papers,
            'average_papers_per_year': avg_papers,
            'peak_year': max_year[0] if max_year else None,
            'peak_papers': max_year[1] if max_year else 0,
            'csv_file': str(csv_filename),
            'chart_file': str(chart_filename) if chart_filename else None
        }
        
        if verbose:
            print("\n" + "=" * 60)
            print("Analysis Summary:")
            print(f"Total papers found: {total_papers:,}")
            print(f"Average papers per year: {avg_papers:,.0f}")
            if max_year:
                print(f"Peak year: {max_year[0]} with {max_year[1]:,} papers")
            print("=" * 60)
        
        return summary

def get_user_input():
    """Interactive prompt for user input"""
    print("🎓 Academic Keyword Analyzer")
    print("=" * 50)
    print("This tool analyzes academic keyword trends using Semantic Scholar API")
    print()
    
    # Get search term
    while True:
        search_term = input("Enter the search term to analyze: ").strip()
        if search_term:
            break
        print("❌ Search term cannot be empty. Please try again.")
    
    # Get start year
    while True:
        try:
            start_year = int(input("Enter start year (e.g., 2020): ").strip())
            if 1800 <= start_year <= datetime.now().year + 1:
                break
            else:
                print(f"❌ Year must be between 1800 and {datetime.now().year + 1}")
        except ValueError:
            print("❌ Please enter a valid year (e.g., 2020)")
    
    # Get end year
    while True:
        try:
            end_year = int(input("Enter end year (e.g., 2023): ").strip())
            if start_year <= end_year <= datetime.now().year + 1:
                break
            else:
                print(f"❌ End year must be between {start_year} and {datetime.now().year + 1}")
        except ValueError:
            print("❌ Please enter a valid year (e.g., 2023)")
    
    # Get optional settings
    print("\n📊 Optional Settings:")
    print("Press Enter to use defaults, or type 'y' to customize")
    
    # Chart generation
    generate_chart = input("Generate histogram chart? (Y/n): ").strip().lower()
    generate_chart = generate_chart != 'n'
    
    # Display plot
    show_plot = True
    if generate_chart:
        show_plot = input("Display the chart interactively? (Y/n): ").strip().lower()
        show_plot = show_plot != 'n'
    
    # Output directory
    output_dir = input("Output directory (press Enter for current directory): ").strip()
    if not output_dir:
        output_dir = "."
    
    # Verbose mode
    verbose = input("Show progress messages? (Y/n): ").strip().lower()
    verbose = verbose != 'n'
    
    return {
        'search_term': search_term,
        'start_year': start_year,
        'end_year': end_year,
        'generate_chart': generate_chart,
        'show_plot': show_plot,
        'output_dir': output_dir,
        'verbose': verbose
    }

def main():
    """Main command-line interface"""
    parser = argparse.ArgumentParser(
        description="Academic Keyword Analyzer - Analyze academic keyword trends using Semantic Scholar API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python academic_keyword_analyzer.py "machine learning" 2020 2023
  python academic_keyword_analyzer.py "blockchain" 2018 2023 --no-chart
  python academic_keyword_analyzer.py "quantum computing" 2015 2023 --output-dir ./results
  python academic_keyword_analyzer.py  # Interactive mode
        """
    )
    
    parser.add_argument('search_term', nargs='?', help='Search term to analyze')
    parser.add_argument('start_year', nargs='?', type=int, help='Start year for analysis')
    parser.add_argument('end_year', nargs='?', type=int, help='End year for analysis')
    parser.add_argument('--output-dir', default='.', help='Output directory for results (default: current directory)')
    parser.add_argument('--no-chart', action='store_true', help='Skip histogram generation')
    parser.add_argument('--no-display', action='store_true', help='Skip displaying the plot')
    parser.add_argument('--quiet', action='store_true', help='Suppress progress messages')
    parser.add_argument('--api-key', help='Semantic Scholar API key (optional)')
    
    args = parser.parse_args()
    
    # Check if running in interactive mode
    if args.search_term is None or args.start_year is None or args.end_year is None:
        # Interactive mode
        try:
            user_input = get_user_input()
            
            # Initialize analyzer
            analyzer = AcademicKeywordAnalyzer(api_key=args.api_key)
            
            # Run analysis
            summary = analyzer.analyze_keyword(
                search_term=user_input['search_term'],
                start_year=user_input['start_year'],
                end_year=user_input['end_year'],
                output_dir=user_input['output_dir'],
                generate_chart=user_input['generate_chart'],
                show_plot=user_input['show_plot'],
                verbose=user_input['verbose']
            )
            
            print(f"\n✅ Analysis complete! Results saved to {user_input['output_dir']}/")
            
        except KeyboardInterrupt:
            print("\n\n❌ Analysis interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            sys.exit(1)
    else:
        # Command-line mode
        # Validate inputs
        if args.start_year > args.end_year:
            print("Error: Start year must be less than or equal to end year")
            sys.exit(1)
        
        if args.start_year < 1800 or args.end_year > datetime.now().year + 1:
            print("Error: Year range must be reasonable (1800 to current year + 1)")
            sys.exit(1)
        
        # Initialize analyzer
        analyzer = AcademicKeywordAnalyzer(api_key=args.api_key)
        
        # Run analysis
        try:
            summary = analyzer.analyze_keyword(
                search_term=args.search_term,
                start_year=args.start_year,
                end_year=args.end_year,
                output_dir=args.output_dir,
                generate_chart=not args.no_chart,
                show_plot=not args.no_display,
                verbose=not args.quiet
            )
            
            print(f"\nAnalysis complete! Results saved to {args.output_dir}/")
            
        except KeyboardInterrupt:
            print("\nAnalysis interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\nError during analysis: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 