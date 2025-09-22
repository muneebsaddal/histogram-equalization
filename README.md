# Histogram Equalization

## Overview
This project implements **Histogram Equalization techniques** for enhancing the contrast of grayscale images.  
Both **global** and **local** methods are explored to demonstrate their effectiveness in improving image details.  

---

## Implemented Methods

1. **Global Histogram Equalization**  
   - Enhances image contrast by redistributing pixel intensities across the full intensity range (0–255).  

2. **Local Histogram Equalization (Tiling Approach)**  
   - Divides the image into smaller tiles.  
   - Performs histogram equalization independently on each tile.  
   - Improves local contrast, especially in regions with varying illumination.  

3. **Local Histogram Equalization (Sliding Window Approach)**  
   - Applies histogram equalization within a sliding window that moves across the image.  
   - Provides smoother results compared to tiling by avoiding block artifacts.  

---
