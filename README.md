# 📊 Paper Keyword Scraper

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Piyushjhu/paper-keyword-scraper)](https://github.com/Piyushjhu/paper-keyword-scraper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Piyushjhu/paper-keyword-scraper)](https://github.com/Piyushjhu/paper-keyword-scraper/network)
[![GitHub issues](https://img.shields.io/github/issues/Piyushjhu/paper-keyword-scraper)](https://github.com/Piyushjhu/paper-keyword-scraper/issues)

A powerful and legitimate tool for analyzing academic keyword trends using the **Semantic Scholar API**. This tool provides comprehensive analysis of academic paper trends by keyword, helping researchers, students, and professionals understand the evolution of research topics over time.

## 🚀 Features

- **🔒 Legitimate API Usage**: Uses the official Semantic Scholar API (no scraping, no TOS violations)
- **⚡ Fast & Reliable**: No rate limiting concerns, completes analysis in seconds
- **📈 Comprehensive Analysis**: Year-by-year paper count analysis with trends
- **📊 Beautiful Visualizations**: Professional histograms with publication-ready quality
- **💾 Multiple Output Formats**: CSV data export and high-resolution PNG charts
- **🎯 Interactive Mode**: User-friendly prompts for easy usage
- **📋 Summary Statistics**: Peak years, averages, and trend analysis
- **🛠️ Flexible Usage**: Both command-line and interactive modes

## 📊 What You Get

- **CSV Data**: Year-by-year paper counts in spreadsheet format
- **Histogram Charts**: Professional bar charts showing trends over time
- **Summary Statistics**: Total papers, averages, peak years, and trends
- **Publication-Ready Output**: High-resolution (300 DPI) charts

## 🛠️ Installation

### Option 1: Clone and Install
```bash
git clone https://github.com/Piyushjhu/paper-keyword-scraper.git
cd paper-keyword-scraper
pip install -r requirements.txt
```

### Option 2: Install as Package
```bash
pip install git+https://github.com/Piyushjhu/paper-keyword-scraper.git
```

## 🎯 Quick Start

### Interactive Mode (Recommended for Beginners)
Simply run the script without arguments:
```bash
python academic_keyword_analyzer.py
```

The tool will guide you through:
1. Entering your search term
2. Setting start and end years
3. Choosing output options
4. Generating results

### Command-Line Mode (For Advanced Users)
```bash
# Basic usage
python academic_keyword_analyzer.py "machine learning" 2020 2023

# Skip chart generation (data only)
python academic_keyword_analyzer.py "blockchain" 2018 2023 --no-chart

# Save results to specific directory
python academic_keyword_analyzer.py "quantum computing" 2015 2023 --output-dir ./results

# Quiet mode (no progress messages)
python academic_keyword_analyzer.py "AI" 2020 2023 --quiet
```

## 📁 Output Files

### CSV Data File
```
machine_learning_2020_2023_results.csv
```
Contains:
```csv
year,paper_count
2020,391368
2021,405022
2022,405445
2023,457559
```

### Histogram Chart
```
machine_learning_2020_2023_histogram.png
```
Features:
- **Professional styling**: Clean, publication-ready appearance
- **High resolution**: 300 DPI suitable for presentations
- **Value labels**: Exact counts displayed on bars
- **Trend visualization**: Clear year-over-year patterns

## 📈 Sample Results

### Analysis Summary
```
============================================================
Analysis Summary:
Total papers found: 1,659,394
Average papers per year: 414,848
Peak year: 2023 with 457,559 papers
============================================================
```

## 🔧 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--output-dir` | Output directory for results | `--output-dir ./results` |
| `--no-chart` | Skip histogram generation | `--no-chart` |
| `--no-display` | Skip displaying the plot | `--no-display` |
| `--quiet` | Suppress progress messages | `--quiet` |
| `--api-key` | Semantic Scholar API key (optional) | `--api-key YOUR_KEY` |

## 🎓 Use Cases

### Academic Research
- **Trend Analysis**: Track research topic popularity over time
- **Literature Reviews**: Understand field growth and evolution
- **Grant Applications**: Demonstrate research area significance
- **Publication Planning**: Identify emerging research areas

### Business Intelligence
- **Market Research**: Identify growing technology trends
- **Competitive Analysis**: Track competitor research focus
- **Investment Decisions**: Understand technology adoption patterns

### Education
- **Curriculum Development**: Identify relevant topics for courses
- **Student Projects**: Guide research topic selection
- **Academic Planning**: Understand field evolution

## 🔍 How It Works

1. **API Integration**: Uses Semantic Scholar's official Graph API
2. **Year-by-Year Search**: Queries each year separately for accurate counts
3. **Data Processing**: Aggregates and validates results
4. **Visualization**: Creates professional charts using matplotlib
5. **Export**: Saves data in multiple formats

## 🌟 Why Semantic Scholar API?

### ✅ Advantages
- **Legitimate**: Official API, no terms of service violations
- **Fast**: No rate limiting, completes in seconds
- **Reliable**: Stable API with good uptime
- **Comprehensive**: Large academic paper database
- **Free**: No cost for basic usage
- **Academic-Focused**: Specialized for research papers

### 📊 Data Quality
- **Accurate Counts**: Real-time data from Semantic Scholar
- **Academic Papers**: Focused on scholarly publications
- **Multiple Sources**: Aggregates from various academic databases
- **Regular Updates**: Database updated frequently

## 🛡️ Legal & Ethical

- ✅ **Compliant**: Uses official API with proper attribution
- ✅ **Respectful**: Includes appropriate delays between requests
- ✅ **Transparent**: Clear about data source and methodology
- ✅ **Educational**: Designed for legitimate research purposes

## 📚 Dependencies

- `requests>=2.25.0`: HTTP requests to Semantic Scholar API
- `matplotlib>=3.5.0`: Chart generation and visualization
- `pandas>=1.3.0`: Data manipulation and CSV export
- `numpy>=1.21.0`: Numerical operations

## 🐛 Troubleshooting

### Common Issues

**"API request failed"**: 
- Check your internet connection
- Verify the API endpoint is accessible
- Try again in a few minutes

**No results found**:
- Check your search term spelling
- Try different variations of the term
- Verify the year range is reasonable

**Chart not displaying**:
- Ensure matplotlib backend is properly configured
- Check that PNG files are generated (they always are)
- Try running with `--no-display` to save without showing

### Getting Help

1. Check the generated CSV file for data
2. Verify the PNG chart was created
3. Try with `--quiet` to see only essential output
4. Ensure your Python environment has all dependencies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the command-line help: `python academic_keyword_analyzer.py --help`
3. Open an issue on GitHub

## 👨‍💻 Author

**Piyush Wanchoo**
- GitHub: [@Piyushjhu](https://github.com/Piyushjhu)
- Email: piyushwanchoo@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Star History

If you find this tool useful, please consider giving it a star on GitHub!

---

**Note**: This tool uses the Semantic Scholar API, which is free and legitimate. No scraping or terms of service violations are involved.
