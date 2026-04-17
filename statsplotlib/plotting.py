# statsplotlib/plotting.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import font_manager
import os

# --- PATH RESOLUTION ---
# This dynamically finds where the package is installed, 
# so it never breaks no matter whose Databricks workspace it runs in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE_PATH = os.path.join(BASE_DIR, "style.mplstyle")
LOGO_PATH = os.path.join(BASE_DIR, "logos/statsports_dark.png")
FONT_DIR = os.path.join(BASE_DIR, "fonts")

def load_custom_fonts():
    """Finds all .ttf and .otf files in the fonts directory and registers them."""
    if os.path.exists(FONT_DIR):
        for font_file in os.listdir(FONT_DIR):
            if font_file.endswith(".ttf") or font_file.endswith(".otf"):
                font_path = os.path.join(FONT_DIR, font_file)
                font_manager.fontManager.addfont(font_path)

def create_branded_plot(figsize=(10, 6), transparent=True, watermark=False):
    """
    Creates a Matplotlib figure/axes with the STATSports style and logo.
    
    Parameters:
    - figsize: Tuple for figure dimensions (width, height)
    - transparent: Boolean. If False, overrides style to use a white background.
    - watermark: Boolean. If True, centers a faded logo in the background instead of the corner.
    """
    # 1. Register fonts before doing anything else
    load_custom_fonts()
    
    # 2. Apply the corporate style sheet
    if os.path.exists(STYLE_PATH):
        plt.style.use(STYLE_PATH)
    else:
        print(f"Warning: Could not find STATSports style at {STYLE_PATH}")
        
    # 3. Create the base canvas
    fig, ax = plt.subplots(figsize=figsize)

    # 4. Background Override 
    if not transparent:
        # We only color the figure background white. 
        # We leave the ax transparent so the watermark can show through!
        fig.patch.set_facecolor('white')

    # 5. Add the Logo Watermark
    if os.path.exists(LOGO_PATH):
        logo = mpimg.imread(LOGO_PATH)
        
        if watermark:
            # FADED CENTER WATERMARK
            # [left, bottom, width, height] - taking up a massive 60% of the plot
            wm_ax = fig.add_axes([0.20, 0.20, 0.60, 0.60], zorder=0)
            wm_ax.imshow(logo, alpha=0.08) # alpha=0.08 makes it extremely subtle/faded
            wm_ax.axis('off')
        else:
            # STANDARD CORNER LOGO
            logo_ax = fig.add_axes([0.78, 0.02, 0.12, 0.12], anchor='SE', zorder=10)
            logo_ax.imshow(logo)
            logo_ax.axis('off')
    
    return fig, ax

def create_branded_subplot(nrows=1, ncols=1, figsize=(12, 8), transparent=True, watermark=False):
    """
    Creates a Matplotlib figure with multiple subplots and STATSports styling.
    
    Parameters:
    - nrows: Number of rows in subplot grid
    - ncols: Number of columns in subplot grid
    - figsize: Tuple for figure dimensions (width, height)
    - transparent: Boolean for background transparency
    - watermark: Boolean for centered faded logo watermark
    
    Returns:
    - fig: Figure object
    - axes: Numpy array of axes objects (or single axis if 1x1)
    """
    load_custom_fonts()
    
    if os.path.exists(STYLE_PATH):
        plt.style.use(STYLE_PATH)
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    
    if not transparent:
        fig.patch.set_facecolor('white')
    
    # Add logo AFTER tight layout (won't be affected by it)
    if os.path.exists(LOGO_PATH):
        logo = mpimg.imread(LOGO_PATH)
        if watermark:
            wm_ax = fig.add_axes([0.20, 0.20, 0.60, 0.60], zorder=0)
            wm_ax.imshow(logo, alpha=0.08)
            wm_ax.axis('off')
        else:
            logo_ax = fig.add_axes([0.78, 0.04, 0.12, 0.12], anchor='SE', zorder=10)
            logo_ax.imshow(logo)
            logo_ax.axis('off')
    
    return fig, axes

def add_branded_title(fig, ax, title_text, subtitle_text=None):
    """
    Applies the correct typography hierarchy to the plot titles.
    Oswald for the main title, Open Sans for the subtitle.
    """
    # INCREASED: pad from 15 to 25 to push the main title higher
    ax.set_title(title_text, fontname="Oswald", fontsize=16, fontweight="bold", loc="left", pad=25)
    
    if subtitle_text:
        # INCREASED: y-coordinate from 1.02 to 1.04 to sit nicely in the gap
        ax.text(0, 1.04, subtitle_text, transform=ax.transAxes, 
                fontname="Open Sans", fontsize=11, color="gray")