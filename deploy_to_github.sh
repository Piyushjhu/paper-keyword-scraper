#!/bin/bash

# Deploy to GitHub Script for Paper Keyword Scraper
# Author: Piyush Wanchoo

echo "🚀 Deploying Paper Keyword Scraper to GitHub..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "academic_keyword_analyzer.py" ]; then
    echo "❌ Please run this script from the project root directory."
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Add all files
echo "📝 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Initial commit: Paper Keyword Scraper - Academic keyword analysis tool using Semantic Scholar API"

# Add remote origin if not exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding remote origin..."
    git remote add origin https://github.com/Piyushjhu/paper-keyword-scraper.git
fi

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "✅ Successfully deployed to GitHub!"
echo "🌐 Your repository is now available at: https://github.com/piyushwanchoo/paper-keyword-scraper"
echo ""
echo "📋 Next steps:"
echo "1. Visit your GitHub repository"
echo "2. Add a description and topics"
echo "3. Enable Issues and Discussions if needed"
echo "4. Share your repository with others!" 