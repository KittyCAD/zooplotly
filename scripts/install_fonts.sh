#!/bin/bash

set -euo pipefail

FONT_DIR="/usr/local/share/fonts"
DOWNLOAD_DIR="downloads"

# Font URLs.
declare -A FONTS=(
    ["OCRA.otf"]="https://raw.githubusercontent.com/opensourcedesign/fonts/master/OCR/OCRA.otf"
    ["SpaceMono-Regular.ttf"]="https://raw.githubusercontent.com/google/fonts/main/ofl/spacemono/SpaceMono-Regular.ttf"
    ["RobotoMono-Regular.ttf"]="https://raw.githubusercontent.com/googlefonts/RobotoMono/main/fonts/ttf/RobotoMono-Regular.ttf"
)

# Create temporary download directory.
mkdir -p "$DOWNLOAD_DIR"

# Download fonts.
for font in "${!FONTS[@]}"; do
    echo "Downloading $font..."
    curl -L -o "$DOWNLOAD_DIR/$font" "${FONTS[$font]}"
done

# Create font directory if it doesn't exist.
sudo mkdir -p "$FONT_DIR"

# Copy fonts to system directory.
echo "Installing fonts..."
sudo cp "$DOWNLOAD_DIR"/* "$FONT_DIR/"

# Update font cache.
echo "Updating font cache..."
sudo fc-cache -f -v

# Clean up downloads.
rm -rf "$DOWNLOAD_DIR"

echo "Font installation complete!"