# DESIGN SYSTEM SPECIFICATION — INDIAN NAVY MDA 2.0
**Project:** National Maritime Domain Awareness & Anomaly Detection System (NMDA 2.0)  
**Classification:** Tactical Command & Intelligence Dashboard  
**Design Paradigm:** Defence C4ISR Tactical Dark Mode / High-Density Mission Control  

---

## 1. Executive Design Vision & Aesthetic Direction

The Indian Navy MDA 2.0 interface is an advanced **tactical command & situational intelligence console** designed for naval operational watch officers, maritime analysts, and strategic command centers.

### Key Aesthetic Principles:
1. **Mission-Critical Clarity**: High contrast, information-dense, zero visual clutter. Every pixel, color, and indicator serves an operational purpose.
2. **Tactical Dark Aesthetic**: Deep oceanic navy and slate tones (`#070d17`, `#0b131e`, `#0f172a`) optimized for low-fatigue 24/7 watchroom operations.
3. **Purposeful Threat Semantics**: Immediate color-coded threat recognition adhering to international naval standards:
   - 🔴 **CRITICAL THREAT (`#ef4444`)**: Dark vessel evasions, unauthorized EEZ incursions, hostile rendezvous.
   - 🟠 **HIGH RISK (`#f97316` / `#f59e0b`)**: Suspicious port loitering, illegal transshipment (STS), AIS position spoofing.
   - 🟡 **MEDIUM / ADVISORY (`#eab308`)**: Minor route deviations, unverified cargo profiles.
   - 🔵 **NORMAL / ACTIVE (`#38bdf8` / `#0284c7`)**: Verified friendly warships, commercial tankers, active vessels.
   - 🟢 **SAFE / CLEARED (`#10b981`)**: OFAC/UN cleared, confirmed NavIC satellite lock, verified port calls.
4. **Authentic Geospatial Restraint**: Zero decorative overland drift; vessel vectors and radar pings strictly observe physical oceanography and maritime sea lanes.

---

## 2. Design Tokens & Color Palette

### 2.1 Surfaces & Backgrounds
```css
:root {
  /* Tactical Canvas Surfaces */
  --bg-deep-ocean: #050a12;      /* Base viewport canvas */
  --bg-panel-primary: #0b131e;    /* Primary sidebar & modal background */
  --bg-panel-secondary: #0f1c2e;  /* Card containers & nested drawers */
  --bg-panel-hover: #16263d;      /* Interactive hover state */
  --bg-glass-overlay: rgba(11, 19, 30, 0.88); /* Backdrop-filter glass panels */
  
  /* Borders & Dividers */
  --border-subtle: #1e293b;       /* Hairline structural separators */
  --border-tactical: #334155;     /* Panel edges & active outlines */
  --border-focus: #38bdf8;        /* Selected vessel / focused input ring */

  /* Text & Typography */
  --text-primary: #f8fafc;        /* High-contrast labels & metrics */
  --text-secondary: #94a3b8;      /* Supporting metadata & timestamps */
  --text-muted: #64748b;          /* Disabled states & secondary legends */
  --text-inverse: #050a12;        /* High-contrast text on bright badges */
}
```

### 2.2 Tactical Threat & Status Palette
```css
:root {
  --threat-critical: #ef4444;    /* Critical Alert / Military Drills */
  --threat-high: #f97316;        /* High Risk / IUU Hot Zones */
  --threat-medium: #f59e0b;      /* Medium Anomaly / Warning */
  --threat-low: #38bdf8;         /* Routine Traffic / Sea Lanes */
  --status-cleared: #10b981;     /* NavIC Locked / Verified Clearance */
  
  /* Strategic Maritime Asset Accents */
  --accent-corridor: #22d3ee;    /* Strategic Shipping Corridors */
  --accent-cables: #8b5cf6;      /* Undersea Cable Infrastructure */
  --accent-straits: #ea580c;     /* International Chokepoints (Hormuz/Malacca) */
  --accent-navic: #06b6d4;       /* Indian NavIC Satellite Telemetry */
}
```

---

## 3. Typography Hierarchy

The typography marries **high-legibility technical sans-serifs** with **monospace data fonts** for telemetry coordinates, MMSI numbers, and timecode stamps.

| Role | Font Family | Size | Weight | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Command Headings** | `'Rajdhani', 'Outfit', sans-serif` | 18px – 22px | 700 / Bold | Top Nav, Modal Headers, Section Titles |
| **Telemetry / Data** | `'JetBrains Mono', 'IBM Plex Mono', monospace` | 11px – 13px | 500 / Medium | MMSI, Lat/Lon, SOG/COG, Timestamps |
| **UI Body / Labels** | `'Segoe UI', 'Inter', -apple-system, sans-serif` | 12px – 14px | 400 / 600 | Cards, tooltips, buttons, logs |
| **Tactical Badges** | `'Rajdhani', 'JetBrains Mono', monospace` | 10px – 11px | 700 / Bold | `CRITICAL`, `STS TRANSFER`, `SPOOFING` |

---

## 4. Component Layout Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TOP COMMAND BAR: System Title | Clearance Passcode Lock | Scan Engine | Unit Metrics    │
├─────────────────┬─────────────────────────────────────────────────┬────────────────────┤
│ LIVE ANOMALIES  │ GEOSPATIAL TACTICAL LEAFLET MAP                 │ SYSTEM LAYERS      │
│ SIDEBAR         │                                                 │ & VESSEL DETAILS   │
│                 │ • Custom Directional SVG Hulls (COG/SOG)        │                    │
│ • Threat Filter │ • Live Extrapolated Motion Vectors              │ • Layer Toggles    │
│ • Anomaly Cards │ • Nautical Sea Lane Polylines (West/East SLOC)   │ • IMO / DWT specs  │
│ • Real-Time SOG │ • Active Radar Threat Pulse Rings               │ • SAR Verification │
│ • Quick Inspect │ • Sub-20ms WebSocket Stream Updates             │ • Track History    │
├─────────────────┴─────────────────────────────────────────────────┴────────────────────┤
│ SHIPBOARD BRIDGE PORTAL / LINK ANALYSIS / TWO-WAY HQ COMMS / FLEET EXPORT MODAL        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Interaction Patterns & Motion Design

1. **Vessel Directional Hull Indicators**:
   - Rotated dynamically matching real-time Course Over Ground ($\text{COG}^\circ$).
   - Vessels with $\text{SOG} > 0.5\text{ kts}$ exhibit an animated wake ring and projected 45-minute dashed motion vectors.
2. **Threat Zone Pulse**:
   - Anomalous vessels trigger a subtle SVG radar ping ring (`threat-zone-pulse`) pulsating with 2.4s ease-in-out period.
3. **Instant Inspection & Focus**:
   - Clicking an alert or vessel smoothly pans the map viewport with animated bounding transitions (`map.setView(..., zoom=8)`).
4. **Two-Way Bridge Communications**:
   - Instant optimistic UI dispatch with acoustic/visual confirmation and timestamped mission log append.
5. **No AI Decorative Tells**:
   - Solid, crisp text colors (no rainbow text-gradients).
   - Minimal, balanced border radii (4px – 8px for military hardware feel).
   - Real-world oceanographic coordinates (no decorative overland artifacts).

---

## 6. Accessibility & Responsive Viewport Rules

- **Contrast Ratios**: Minimum 7:1 ratio for critical telemetry data and 4.5:1 for body copy against dark backgrounds.
- **Keyboard Navigation**: Full focus trap within modals (Lock Screen, Comms Drawer, Intelligence Export).
- **Responsive Layout**: Fluid breakpoints supporting dual-screen tactical monitors ($1920\times1080$, $2560\times1440$, $4\text{K}$) and responsive collapse for 13" tactical field laptops.
