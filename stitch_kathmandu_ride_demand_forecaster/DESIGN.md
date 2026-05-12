---
name: Kathmandu Ride Demand Forecaster
colors:
  surface: '#0e1416'
  surface-dim: '#0e1416'
  surface-bright: '#343a3c'
  surface-container-lowest: '#090f11'
  surface-container-low: '#171c1f'
  surface-container: '#1b2023'
  surface-container-high: '#252b2d'
  surface-container-highest: '#303638'
  on-surface: '#dee3e6'
  on-surface-variant: '#bcc9ce'
  inverse-surface: '#dee3e6'
  inverse-on-surface: '#2b3134'
  outline: '#869398'
  outline-variant: '#3d494d'
  surface-tint: '#4cd6fb'
  primary: '#4cd6fb'
  on-primary: '#003642'
  primary-container: '#00b4d8'
  on-primary-container: '#00414f'
  inverse-primary: '#00677d'
  secondary: '#ffb59d'
  on-secondary: '#5d1900'
  secondary-container: '#b83900'
  on-secondary-container: '#ffddd2'
  tertiary: '#ffb77d'
  on-tertiary: '#4d2600'
  tertiary-container: '#eb8f3b'
  on-tertiary-container: '#5d2f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b3ebff'
  primary-fixed-dim: '#4cd6fb'
  on-primary-fixed: '#001f27'
  on-primary-fixed-variant: '#004e5f'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#ffb59d'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#832600'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#0e1416'
  on-background: '#dee3e6'
  surface-variant: '#303638'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 30px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-desktop: 32px
  container-padding-mobile: 16px
  gutter: 24px
  card-gap: 16px
---

## Brand & Style

The visual identity of the design system is rooted in the intersection of high-velocity data and the cultural fabric of Kathmandu. It targets urban planners and fleet managers who require high-precision forecasting tools. The brand personality is **authoritative, analytical, and futuristic**, yet deeply grounded in its geographical context.

The aesthetic follows a **Premium Glassmorphism** approach. It utilizes deep, multi-layered backgrounds to simulate depth, while UI elements appear as frosted glass panes. To differentiate this design system, we integrate subtle cultural motifs—specifically geometric patterns inspired by *Dhaka* weaving and the structural symmetry of Newari windows—as low-opacity background textures and decorative strokes on primary containers. This creates a high-tech "Cyber-Kathmandu" atmosphere that feels both professional and culturally resonant.

## Colors

The palette is optimized for long-session data analysis in low-light environments. 

- **Primary Accent (Electric Blue):** Reserved for "Flow" and "Growth" indicators, active states, and primary CTAs. It represents the fluid movement of traffic.
- **Secondary Accent (Vibrant Orange):** Used for "Peak Demand," heatmaps, and urgent alerts. It draws inspiration from the warm evening glow of Kathmandu's streetlights.
- **Surface Strategy:** We avoid pure black to maintain depth. The background is a Deep Navy, while cards use a semi-transparent layer with a `backdrop-filter: blur(12px)`.
- **Cultural Accents:** A specialized "Mandala Gold" (#d4af37) may be used sparingly for premium iconography or status achievements to honor the local heritage.

## Typography

This design system utilizes **Inter** for its neutral, highly legible characteristics, ensuring that dense data tables and complex dashboards remain readable. 

To reinforce the technical nature of the forecaster, we introduce **JetBrains Mono** for data labels, coordinates, and timestamps. This secondary font adds a "terminal" aesthetic that suggests precision. Headings should utilize tighter letter spacing to maintain a compact, professional look, while labels use expanded spacing for better scannability at small sizes.

## Layout & Spacing

The layout follows a **12-column fluid grid** for desktop, collapsing to a single column for mobile devices. 

- **Data Density:** We employ a tight 8px spacing rhythm to maximize information density without cluttering the UI.
- **Negative Space:** While the UI is data-heavy, we use "breathing room" around glass cards to ensure the background cultural motifs are visible, creating a sense of layered depth.
- **Sidebars:** A fixed 280px left navigation sidebar uses a high-blur glass effect to separate global controls from the main dashboard workspace.

## Elevation & Depth

Elevation is conveyed through **transparency and blur intensity** rather than traditional drop shadows.

1.  **Level 0 (Base):** Deep Navy background with subtle, large-scale topographic map patterns of the Kathmandu Valley at 5% opacity.
2.  **Level 1 (Cards):** 65% opacity surfaces with a 1px solid border (top-left light source simulation) and `backdrop-filter: blur(12px)`.
3.  **Level 2 (Modals/Popovers):** 85% opacity surfaces with a more pronounced white-to-transparent gradient border and a deep 40px ambient shadow tinted with the Primary Accent color at 10% opacity.

## Shapes

We use a **Rounded** (Level 2) shape language to soften the "industrial" feel of the data. 

Standard cards and buttons feature a 0.5rem (8px) corner radius. For larger dashboard containers, we scale this to 1rem (16px). This moderate rounding strikes a balance between professional rigor and modern approachability. Cultural motifs integrated into borders should follow these radius constraints to ensure visual harmony.

## Components

- **Glass Buttons:** Primary buttons use a solid Electric Blue fill. Secondary buttons use a glass background with a high-contrast Electric Blue border.
- **Forecasting Charts:** Line graphs use glowing paths (Neon glow effect) in Electric Blue for predicted demand and Orange for historical peaks.
- **Data Chips:** Small, pill-shaped labels with a 10% background tint of the status color (e.g., Green for 'High Accuracy', Orange for 'High Demand').
- **Cultural Dividers:** Instead of simple lines, horizontal dividers can occasionally feature a 2px tall repeated geometric pattern inspired by Himalayan architecture.
- **Input Fields:** Minimalist glass inputs with a bottom-only border that illuminates to Electric Blue on focus.
- **Heatmap Cards:** Specialized cards that use high-contrast color scales from Deep Navy to Vibrant Orange to visualize ride density across city wards.