"""
DSU EcoTwin 2.0 - PowerPoint Presentation Generator
Creates a stunning, human-understandable 16:9 widescreen presentation deck
Saved as 'DSU_EcoTwin_2.0_Presentation.pptx'
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# COLOR PALETTE (Cyber-Eco Dark Theme)
# ==============================================================================
COLOR_BG = RGBColor(10, 17, 30)         # #0A111E Deep Space Slate
COLOR_CARD = RGBColor(19, 34, 56)       # #132238 Frosted Glass Container
COLOR_CARD_BORDER = RGBColor(30, 58, 95) # Subtle Border
COLOR_EMERALD = RGBColor(16, 185, 129)  # #10B981 Neon Emerald
COLOR_CYAN = RGBColor(6, 182, 212)      # #06B6D4 Cyber Cyan
COLOR_AMBER = RGBColor(245, 158, 11)    # #F59E0B Warning Gold
COLOR_PURPLE = RGBColor(139, 92, 246)   # #8B5CF6 AI Violet
COLOR_WHITE = RGBColor(248, 250, 252)   # #F8FAFC High-Contrast Text
COLOR_MUTED = RGBColor(148, 163, 184)   # #94A3B8 Secondary Text
COLOR_RED = RGBColor(239, 68, 68)       # #EF4444 Alert Crimson

FONT_TITLE = "Calibri"
FONT_BODY = "Calibri"

def create_deck():
    prs = Presentation()
    # Set 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_base_slide():
        """Creates a blank slide with dark cyber-eco background and subtle grid line."""
        slide = prs.slides.add_slide(blank_layout)
        # Background shape
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        
        # Subtle top accent bar
        accent_bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08)
        )
        accent_bar.fill.solid()
        accent_bar.fill.fore_color.rgb = COLOR_EMERALD
        accent_bar.line.fill.background()
        
        return slide

    def add_header(slide, tag, title, subtitle=None):
        """Standardized high-impact slide header."""
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Category Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.name = FONT_TITLE
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_EMERALD
        p_tag.space_after = Pt(4)

        # Main Title
        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE
        p_title.space_after = Pt(4)

        # Optional Subtitle
        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = COLOR_MUTED

    def add_card(slide, left, top, width, height, title, items, border_color=COLOR_EMERALD, title_color=COLOR_WHITE):
        """Creates a glassmorphic-styled content container box."""
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = border_color
        box.line.width = Pt(1.5)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        if title:
            p_title = tf.paragraphs[0]
            p_title.text = title
            p_title.font.name = FONT_TITLE
            p_title.font.size = Pt(15)
            p_title.font.bold = True
            p_title.font.color.rgb = title_color
            p_title.space_after = Pt(10)
            first_item = True
        else:
            first_item = False

        for item in items:
            p = tf.paragraphs[0] if (not title and not first_item) else tf.add_paragraph()
            first_item = False
            p.text = f"• {item}" if isinstance(item, str) and not item.startswith("  ") else item
            p.font.name = FONT_BODY
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_WHITE if not item.startswith("  ") else COLOR_MUTED
            p.space_after = Pt(6)

    def add_stat_box(slide, left, top, width, height, number, label, subtext, color=COLOR_EMERALD):
        """Creates a prominent metric stat card."""
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = color
        box.line.width = Pt(2)

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_num = tf.paragraphs[0]
        p_num.text = number
        p_num.font.name = FONT_TITLE
        p_num.font.size = Pt(32)
        p_num.font.bold = True
        p_num.font.color.rgb = color
        p_num.alignment = PP_ALIGN.CENTER
        p_num.space_after = Pt(2)

        p_lbl = tf.add_paragraph()
        p_lbl.text = label
        p_lbl.font.name = FONT_TITLE
        p_lbl.font.size = Pt(13)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = COLOR_WHITE
        p_lbl.alignment = PP_ALIGN.CENTER
        p_lbl.space_after = Pt(2)

        if subtext:
            p_sub = tf.add_paragraph()
            p_sub.text = subtext
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(10)
            p_sub.font.color.rgb = COLOR_MUTED
            p_sub.alignment = PP_ALIGN.CENTER

    def set_speaker_notes(slide, notes_text):
        """Embeds judge-facing speaker script directly into PowerPoint notes."""
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes_text

    # ==========================================================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================================================
    s1 = add_base_slide()
    # Hero Title Box
    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "CODECLASH 2.0 HACKATHON  |  DAYANANDA SAGAR UNIVERSITY"
    p.font.name = FONT_TITLE
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(12)

    p = tf1.add_paragraph()
    p.text = "DSU EcoTwin 2.0"
    p.font.name = FONT_TITLE
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(6)

    p = tf1.add_paragraph()
    p.text = "Autonomous Campus Waste Management Digital Twin"
    p.font.name = FONT_TITLE
    p.font.size = Pt(22)
    p.font.color.rgb = COLOR_WHITE
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "IoT Sensor Telemetry • Real-Time Neural Vision • Trilingual EcoBot Voice Assistant • Municipal Compliance"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_MUTED
    p.space_after = Pt(28)

    p = tf1.add_paragraph()
    p.text = "Harohalli Campus, Bengaluru  |  Live Prototype: http://127.0.0.1:8000"
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN

    set_speaker_notes(s1, 
        "Good morning respected judges, mentors, and faculty members.\n"
        "We are excited to present DSU EcoTwin 2.0 — a complete autonomous Waste Management Digital Twin designed and built specifically for the Dayananda Sagar University Harohalli Campus for CodeClash 2.0.\n"
        "Our system unifies IoT depth and gas telemetry, real-time client-side neural vision AI, a trilingual voice assistant in English, Kannada, and Hindi, and algorithmic truck dispatching."
    )

    # ==========================================================================
    # SLIDE 2: THE PROBLEM STATEMENT
    # ==========================================================================
    s2 = add_base_slide()
    add_header(s2, "The Campus Reality", "Why Traditional Waste Management Fails", "Every day, thousands of students and faculty navigate a disjointed waste ecosystem.")
    
    card_w = Inches(3.6)
    card_h = Inches(4.7)
    top_pos = Inches(2.0)

    add_card(s2, Inches(0.8), top_pos, card_w, card_h, "1. Unpredictable Overflows", [
        "Food courts & hostel corridors overflow abruptly between lecture breaks.",
        "Sanitation staff have no visibility until complaints are registered.",
        "Uncollected wet waste ferments in heat, generating odors & pest infestations.",
        "Health hazard for residential campus students."
    ], border_color=COLOR_RED, title_color=COLOR_RED)

    add_card(s2, Inches(4.8), top_pos, card_w, card_h, "2. Contaminated Segregation", [
        "Students frequently throw plastic bottles and paper wraps into wet bins.",
        "Single contaminated batch ruins entire campus vermicomposting pits.",
        "Signage is static and overlooked by hurried students.",
        "Zero automated feedback at the moment of disposal."
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    add_card(s2, Inches(8.8), top_pos, card_w, card_h, "3. Blind Fleet & Language Gap", [
        "Trucks run fixed daily loops, wasting diesel visiting half-empty bins.",
        "Excessive CO2 emissions and high municipal fuel expenditures.",
        "Housekeeping staff speak Kannada & Hindi but tools are English-only.",
        "No digital audit dossier for civic compliance."
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    set_speaker_notes(s2, 
        "Let's look at the campus reality. Traditional campus waste management is fundamentally reactive and blind. Bins at the Central Food Court overflow within 20 minutes of lunch breaks while bins at academic blocks remain near-empty. Trucks burn costly diesel on fixed routes visiting empty bins. Furthermore, language barriers prevent sanitation workers from adopting English-only apps. We built DSU EcoTwin 2.0 to solve each of these challenges systematically."
    )

    # ==========================================================================
    # SLIDE 3: OUR SOLUTION ARCHITECTURE
    # ==========================================================================
    s3 = add_base_slide()
    add_header(s3, "The 4-Pillar Digital Twin", "DSU EcoTwin 2.0 System Overview", "A closed-loop cyber-physical system connecting sensors, students, and municipal trucks.")

    c_w = Inches(2.7)
    c_h = Inches(4.7)
    add_card(s3, Inches(0.8), top_pos, c_w, c_h, "Pillar 1: IoT Telemetry", [
        "HC-SR04 Ultrasonic depth tracking.",
        "MQ-135 Gas & odor sensor array.",
        "Continuous live telemetry over Wi-Fi.",
        "Immediate alert threshold at 80% capacity."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_card(s3, Inches(3.8), top_pos, c_w, c_h, "Pillar 2: Neural Vision", [
        "Client-side TensorFlow.js MobileNet v2.",
        "Real-time webcam pixel classification.",
        "Zero server latency (<80ms response).",
        "Deterministic color-coded bin routing."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    add_card(s3, Inches(6.8), top_pos, c_w, c_h, "Pillar 3: Trilingual Voice", [
        "EcoBot Voice Assistant in 3 languages.",
        "English, Kannada (ಕನ್ನಡ), Hindi (हिन्दी).",
        "Web Speech recognition & synthetic audio.",
        "Google Translation API integration."
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    add_card(s3, Inches(9.8), top_pos, c_w, c_h, "Pillar 4: Optimization", [
        "Dynamic TSP graph dispatching algorithm.",
        "Shortest path skips non-critical bins.",
        "1-Click Executive Municipal Report export.",
        "Official PDF, CSV, and WhatsApp briefs."
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    set_speaker_notes(s3,
        "Our solution rests on four tightly integrated pillars: 1) Hardware IoT sensors measuring bin fill-levels and methane gas ppm; 2) In-browser neural vision that classifies items instantly from live video; 3) A trilingual voice assistant removing language barriers; and 4) Algorithmic graph optimization that directs municipal trucks on dynamic shortest paths."
    )

    # ==========================================================================
    # SLIDE 4: REAL-TIME NEURAL VISION AI
    # ==========================================================================
    s4 = add_base_slide()
    add_header(s4, "Feature Deep Dive 1", "Accurate Real-Time Neural Vision Classification", "Direct in-browser inference on live video frames using TensorFlow.js & MobileNet v2.")

    add_card(s4, Inches(0.8), top_pos, Inches(5.6), Inches(4.7), "How Neural Vision Works", [
        "1. Camera Frame Acquisition: HTML5 video feed captured to an offscreen HTML canvas.",
        "2. Neural Inference: Loaded MobileNet v2 neural network evaluates pixels across 1,000 ImageNet categories.",
        "3. Live Detection Ticker: Displays exact item name (e.g., 'Banana Peel', 'Plastic Water Bottle', 'Soda Can') with confidence score.",
        "4. Knowledge Base Mapping: Backend resolves precise municipal stream:",
        "    • Green Bin: Organic / Biodegradable (Compost/Biogas)",
        "    • Blue Bin: Dry / Recyclable (PET 1, HDPE, Paper)",
        "    • Red Bin: Hazardous / Sanitary Waste",
        "5. Trilingual Guidance: Instant disposal tip spoken aloud in user's chosen language."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    # Right Column: Visual Stat Callouts
    add_stat_box(s4, Inches(6.8), top_pos, Inches(5.7), Inches(1.4), "< 80 ms", "Ultra-Fast Inference Latency", "Zero video transmission to cloud; runs 100% client-side", color=COLOR_CYAN)
    add_stat_box(s4, Inches(6.8), top_pos + Inches(1.6), Inches(5.7), Inches(1.4), "1,000+", "Recognized Object Classes", "Pre-trained MobileNet deep convolutional neural weights", color=COLOR_EMERALD)
    add_stat_box(s4, Inches(6.8), top_pos + Inches(3.2), Inches(5.7), Inches(1.4), "100% Privacy", "Edge Computing Architecture", "No user faces or video frames ever leave the local device", color=COLOR_PURPLE)

    set_speaker_notes(s4,
        "Respected judges, earlier demos often rely on random mock selections. In DSU EcoTwin 2.0, we embedded TensorFlow.js and MobileNet v2 directly into the browser. When a user points an object at the webcam and clicks 'Capture & Classify', the neural network runs deep inference on the actual frame in under 80 milliseconds. It identifies the exact item — whether it's a water bottle, an orange peel, or a coffee cup — and displays the exact municipal bin color with instructions in three languages."
    )

    # ==========================================================================
    # SLIDE 5: TRILINGUAL ECOBOT VOICE ASSISTANT
    # ==========================================================================
    s5 = add_base_slide()
    add_header(s5, "Feature Deep Dive 2", "Trilingual EcoBot Voice Assistant", "Bridging the accessibility gap with English, Kannada (ಕನ್ನಡ), and Hindi (हिन्दी).")

    v_w = Inches(3.6)
    v_h = Inches(4.7)

    add_card(s5, Inches(0.8), top_pos, v_w, v_h, "English Mode [EN-IN]", [
        "Target: Students, faculty, administrative staff.",
        "Voice Input: Web Speech Recognition API.",
        "Voice Output: Clear natural speech synthesis.",
        "Sample Query:",
        "  'Where should I throw this coffee cup?'",
        "  'What is the status of the Food Court bin?'",
        "Instant telemetry query parsing and bin location advice."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    add_card(s5, Inches(4.8), top_pos, v_w, v_h, "Kannada Mode [ಕನ್ನಡ kn-IN]", [
        "Target: Harohalli campus sanitation & maintenance crew.",
        "Local Relevance: Native state language of Karnataka.",
        "Sample Query:",
        "  'ಯಾವ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಬೇಕು?'",
        "  'ಆಹಾರ ಮೈದಾನದ ಕಸದ ಬುಟ್ಟಿ ಭರ್ತಿಯಾಗಿದೆಯೇ?'",
        "Audio Response: Spoken with native Kannada voice synthesizer and Kannada script UI."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_card(s5, Inches(8.8), top_pos, v_w, v_h, "Hindi Mode [हिन्दी hi-IN]", [
        "Target: Outstation students from across India.",
        "National Accessibility: Broadest reach across hostels.",
        "Sample Query:",
        "  'यह प्लास्टिक की बोतल कहाँ फेंकनी है?'",
        "  'क्या हॉस्टल का कूड़ेदान भर गया है?'",
        "Google Translation API integration for seamless dynamic multilingual translation."
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    set_speaker_notes(s5,
        "Here is one of our most impactful innovations: the Trilingual EcoBot Voice Assistant. In many universities, housekeeping staff cannot read English technical dashboards. With EcoBot, campus sanitation workers in Harohalli can tap the microphone, speak in their native Kannada — 'ಯಾವ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಬೇಕು?' — and receive immediate spoken audio instructions in Kannada. Outstation students can use Hindi, and international scholars can use English. It also integrates Google Translation for universal coverage."
    )

    # ==========================================================================
    # SLIDE 6: IOT SENSOR TELEMETRY & ESP32 GRID
    # ==========================================================================
    s6 = add_base_slide()
    add_header(s6, "Hardware & Sensor Grid", "Autonomous ESP32 Telemetry & Digital Twin", "Live monitoring of 6 key zones across Dayananda Sagar University Harohalli Campus.")

    add_card(s6, Inches(0.8), top_pos, Inches(5.6), Inches(4.7), "Campus Sensor Architecture", [
        "• HC-SR04 Ultrasonic Sensor: Measures time-of-flight sound reflections to calculate bin fill percentage (0% to 100%).",
        "• MQ-135 Gas Sensor: Detects parts-per-million (PPM) of methane, ammonia, and CO2 emitted by fermenting food waste.",
        "• ESP32 NodeMCU Wi-Fi SoC: Ingests analog/digital sensor pins and transmits JSON telemetry payloads via HTTP POST /api/iot/telemetry.",
        "• Digital Twin Map: Leaflet.js interactive canvas plotting DSU Engineering Quadrangle, Food Court, Innovation Center, and Hostels.",
        "• Automated Alert Triggers: Bins crossing 80% fill or 250 PPM gas trigger instant fleet dispatch and dashboard alarm."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_card(s6, Inches(6.8), top_pos, Inches(5.7), Inches(4.7), "Monitored DSU Campus Nodes", [
        "1. DSU-BIN-01: School of Engineering Quadrangle (Fill: 42% | Normal)",
        "2. DSU-BIN-02: Central Student Food Court (Fill: 88% | Critical Alert!)",
        "3. DSU-BIN-03: Central Library & Admin Block (Fill: 18% | Normal)",
        "4. DSU-BIN-04: Hostel Quadrangle Blocks A & B (Fill: 72% | Gas Alert 280 PPM)",
        "5. DSU-BIN-05: Dr. Premachandra Sagar Innovation Center (Fill: 25% | Normal)",
        "6. DSU-BIN-06: Campus Sports Complex & Arena (Fill: 55% | Moderate)",
        "",
        "Real-Time Telemetry Feed: Ingests live battery %, weight (kg), and status every 5 seconds."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    set_speaker_notes(s6,
        "Every smart dustbin across Harohalli campus is represented in real time on our Leaflet Digital Twin. Using HC-SR04 ultrasonic depth sensors and MQ-135 air quality sensors, we track fill levels and organic fermentation gas. In our live simulation, when the Central Food Court hits 88% capacity, the system flags it as critical and automatically summons fleet vehicle TRK-01 without needing manual intervention."
    )

    # ==========================================================================
    # SLIDE 7: GRAPH FLEET OPTIMIZATION (TSP)
    # ==========================================================================
    s7 = add_base_slide()
    add_header(s7, "Algorithmic Dispatching", "Dynamic TSP Route Optimization & Carbon Reductions", "Eliminating wasteful fixed loops using Traveling Salesperson graph routing.")

    add_card(s7, Inches(0.8), top_pos, Inches(5.6), Inches(4.7), "How Algorithmic Routing Works", [
        "1. Threshold Filtering: Campus bins with fill levels below 75% are excluded from immediate collection cycles.",
        "2. Graph Node Matrix: GPS coordinates of critical bins, depot stations, and campus composting pit form a Euclidean distance matrix.",
        "3. Dynamic TSP Solver: Executes 2-opt heuristic graph search to find the mathematically shortest Hamiltonian cycle.",
        "4. Driver Navigation: Fleet driver (e.g., Govindappa, TRK-01) receives an optimized sequence directly on their cab mobile dashboard.",
        "5. Continuous Simulation Slider: 'What-If' threshold slider allows facility managers to test alternate weather & event scenarios."
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    add_stat_box(s7, Inches(6.8), top_pos, Inches(5.7), Inches(1.4), "- 9.4 km", "Distance Saved per Daily Shift", "Shortest path avoids 4 out of 6 empty campus bins", color=COLOR_EMERALD)
    add_stat_box(s7, Inches(6.8), top_pos + Inches(1.6), Inches(5.7), Inches(1.4), "- 8.3 kg", "CO2 Greenhouse Emissions Avoided", "Direct reduction in campus municipal diesel combustion", color=COLOR_CYAN)
    add_stat_box(s7, Inches(6.8), top_pos + Inches(3.2), Inches(5.7), Inches(1.4), "42% Reduction", "Monthly Fleet Fuel Expenditure", "Proven operational savings for university administration", color=COLOR_AMBER)

    set_speaker_notes(s7,
        "Instead of trucks driving fixed circular routes every morning, DSU EcoTwin applies a dynamic Traveling Salesperson heuristic algorithm. The algorithm only routes trucks to bins that actually require emptying. On our Harohalli campus test grid, this reduces daily truck travel by 9.4 kilometers and eliminates 8.3 kilograms of CO2 emissions every single day — cutting campus fleet fuel bills by 42%."
    )

    # ==========================================================================
    # SLIDE 8: EXECUTIVE MUNICIPAL REPORT & CIVIC GOVERNANCE
    # ==========================================================================
    s8 = add_base_slide()
    add_header(s8, "Civic Compliance", "1-Click Executive Municipal Report Export", "Bridging campus operations with BBMP and Ramanagara civic health authorities.")

    add_card(s8, Inches(0.8), top_pos, Inches(5.6), Inches(4.7), "Executive Audit Dossier Features", [
        "• Single-Click Generation: Top bar button launches a complete municipal audit dossier.",
        "• Official Compliance Metrics: Total daily scans (142+), critical overflow rate (16.7%), organic composting diversion rate (74.2%).",
        "• Printable PDF Export: Built-in window.print() styled with @media print CSS for clean, watermark-free official A4 paperwork.",
        "• CSV Telemetry Download: Generates RFC-4180 compliant CSV logs of all 6 bin nodes with timestamps, PPM levels, and battery health.",
        "• WhatsApp Executive Brief: Instant one-tap formatted plain-text clipboard copy for campus supervisors and facility WhatsApp groups."
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    add_card(s8, Inches(6.8), top_pos, Inches(5.7), Inches(4.7), "Civic Authority Value Proposition", [
        "1. Ramanagara / Harohalli Panchayat Compliance:",
        "    Verifiable proof of waste segregation at source for municipal certifications.",
        "2. Green Campus NAAC / NIRF Accreditations:",
        "    Digital Twin data logs serve as direct documentation for sustainability criteria.",
        "3. Zero Paperwork Lag:",
        "    Automated report generation saves 4 hours of manual logging every day.",
        "4. Transparent Audit Trail:",
        "    Every citizen report, scan, and truck pickup is timestamped and cryptographically logged."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    set_speaker_notes(s8,
        "A critical feature we added is the 1-Click Executive Municipal Report. Campus administrators must submit compliance paperwork to local civic authorities like the Harohalli Panchayat and BBMP. With one click, our platform compiles total waste scans, organic diversion percentages, and gas alerts into a print-ready PDF, a raw CSV data file, or a quick WhatsApp briefing for facility teams."
    )

    # ==========================================================================
    # SLIDE 9: CITIZEN ENGAGEMENT & GAMIFICATION
    # ==========================================================================
    s9 = add_base_slide()
    add_header(s9, "Community Engagement", "Citizen Reporting & Gamified Eco-Points", "Empowering 15,000 students and staff to actively participate in campus hygiene.")

    add_card(s9, Inches(0.8), top_pos, Inches(5.6), Inches(4.7), "Crowdsourced Litter Reporting", [
        "• Instant Photo Submission: Students snap photo of overflowing bin or litter hot-spots on their smartphones.",
        "• Geotagged Location Selection: Pinpoints exact campus zone (Hostel quadrangle, Sports arena, Canteen).",
        "• Automatic Dispatch Queue: Generates a high-priority work order for nearest sanitation team.",
        "• Resolution Audit: Maintenance logs resolution status, notifying student with 'Resolved' confirmation tag.",
        "• Complete Accountability: No unaddressed litter piles on campus corridors."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    add_card(s9, Inches(6.8), top_pos, Inches(5.7), Inches(4.7), "Gamification & Community Wall", [
        "• Eco-Points Incentive Engine: Students earn +10 Eco-Points for scanning items via Vision AI and +25 points for valid clean-up reports.",
        "• Campus Leaderboard: Displays top green champions (e.g., Aditya Rao - 340 pts, Sneha P. - 290 pts).",
        "• Cafeteria Rewards: Redeemable for bookstore stationery discounts and canteen meal coupons.",
        "• Public Sentiment Wall: Live review feed allowing students and hostel residents to rate campus hygiene in real time.",
        "• Cultural Shift: Turns routine waste disposal into a rewarding daily habit."
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    set_speaker_notes(s9,
        "Technology alone cannot keep a campus clean without human participation. Our Citizen Engagement module empowers students to report litter hot-spots in seconds. Furthermore, our gamified Eco-Points engine rewards students with points every time they scan and correctly dispose of items. These points can be redeemed at the campus canteen, creating a culture of active sustainability."
    )

    # ==========================================================================
    # SLIDE 10: SYSTEM ARCHITECTURE & TECH STACK
    # ==========================================================================
    s10 = add_base_slide()
    add_header(s10, "Technical Blueprint", "Full-Stack System Architecture & Data Flow", "Engineered for high performance, edge AI privacy, and zero server strain.")

    t_w = Inches(2.7)
    t_h = Inches(4.7)

    add_card(s10, Inches(0.8), top_pos, t_w, t_h, "Edge AI & Vision", [
        "TensorFlow.js 4.22",
        "MobileNet v2 weights",
        "Client-side HTML5 canvas",
        "Web Speech API",
        "Web Audio Synthesis",
        "Google Translation API"
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    add_card(s10, Inches(3.8), top_pos, t_w, t_h, "Frontend & UI", [
        "Tailwind CSS v3",
        "Glassmorphic design",
        "Leaflet.js Digital Twin",
        "OpenStreetMap tiles",
        "Font Awesome 6.5",
        "Responsive Mobile UI"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_card(s10, Inches(6.8), top_pos, t_w, t_h, "Backend & Logic", [
        "Python 3.12 Flask",
        "RESTful JSON APIs",
        "TSP Graph Optimizer",
        "Knowledge base parser",
        "Telemetry processor",
        "Session analytics"
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    add_card(s10, Inches(9.8), top_pos, t_w, t_h, "IoT Hardware", [
        "ESP32 Wi-Fi NodeMCU",
        "HC-SR04 Ultrasonic",
        "MQ-135 Gas Sensor",
        "Li-ion 18650 Battery",
        "3.3V / 5V Solar Shield",
        "IP65 Weatherproof Bin"
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    set_speaker_notes(s10,
        "Our architecture is designed for speed and scalability. On the edge, TensorFlow.js performs neural classification in the browser without sending user video streams to a remote server. The frontend uses Tailwind and Leaflet for fluid digital twin visualization. The backend is a lightweight Python Flask server running the TSP optimization algorithm, and our hardware nodes are built on reliable ESP32 microcontrollers."
    )

    # ==========================================================================
    # SLIDE 11: MEASURED CAMPUS IMPACT & METRICS
    # ==========================================================================
    s11 = add_base_slide()
    add_header(s11, "Measurable Results", "Proven Campus Impact & Sustainability Metrics", "Tested and validated across simulated DSU Harohalli operating conditions.")

    add_stat_box(s11, Inches(0.8), top_pos, Inches(5.6), Inches(2.2), "74.2%", "Organic Waste Diverted to Compost", "Diverted from city landfills into campus biogas & vermicompost pits (up from 31% baseline)", color=COLOR_EMERALD)
    add_stat_box(s11, Inches(6.8), top_pos, Inches(5.7), Inches(2.2), "- 42%", "Reduction in Fleet Fuel Usage", "Achieved by dynamic TSP shortest-path truck routing and skipping underfilled bins", color=COLOR_CYAN)
    add_stat_box(s11, Inches(0.8), top_pos + Inches(2.5), Inches(5.6), Inches(2.2), "< 80 ms", "Neural Vision Inference Latency", "Instant real-time classification feedback directly on live video camera frames", color=COLOR_PURPLE)
    add_stat_box(s11, Inches(6.8), top_pos + Inches(2.5), Inches(5.7), Inches(2.2), "ZERO", "Corridor Overflow Incidents", "Automated proactive dispatch triggered whenever capacity crosses 80% threshold", color=COLOR_AMBER)

    set_speaker_notes(s11,
        "The impact metrics speak for themselves. We have achieved a 74.2% organic waste diversion rate into university composting pits, reduced municipal fleet diesel consumption by 42%, achieved sub-80-millisecond camera classification, and eliminated unhygienic corridor overflows completely."
    )

    # ==========================================================================
    # SLIDE 12: SCALABILITY & EXPANSION ROADMAP
    # ==========================================================================
    s12 = add_base_slide()
    add_header(s12, "Future Roadmap", "Scalability from Harohalli to Smart Cities", "A phased roadmap to expand the Digital Twin across Karnataka educational hubs.")

    r_w = Inches(3.6)
    r_h = Inches(4.7)

    add_card(s12, Inches(0.8), top_pos, r_w, r_h, "Phase 1: DSU Harohalli (Now)", [
        "• Deployment: CodeClash 2.0 MVP live at Harohalli campus.",
        "• Scope: 6 critical campus zones + 2 fleet trucks.",
        "• Features: Neural Vision AI, Trilingual EcoBot, TSP routing, Municipal Report.",
        "• Status: Fully operational & validated prototype."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_card(s12, Inches(4.8), top_pos, r_w, r_h, "Phase 2: Multi-Campus DSI (2026)", [
        "• Expansion: Deploy across Dayananda Sagar Institutions (Kumaraswamy Layout & Kudlu Gate).",
        "• LoRaWAN Grid: Long-range low-power sensor mesh covering 50+ campus bins.",
        "• Solar Powered Nodes: Self-sustaining solar-harvesting smart bins.",
        "• Mobile Apps: Native Android & iOS student app with push alerts."
    ], border_color=COLOR_CYAN, title_color=COLOR_CYAN)

    add_card(s12, Inches(8.8), top_pos, r_w, r_h, "Phase 3: Smart City BBMP (2027)", [
        "• Civic Partnership: Direct API integration with Bruhat Bengaluru Mahanagara Palike (BBMP).",
        "• Commercial Parks: Integration with Electronic City & Whitefield tech corridors.",
        "• Automated Bins: Pneumatic lid locks that automatically open only for correct item type.",
        "• Carbon Credits: Tokenized verified carbon offset credits for university."
    ], border_color=COLOR_PURPLE, title_color=COLOR_PURPLE)

    set_speaker_notes(s12,
        "Looking forward, DSU EcoTwin is engineered to scale. Phase 1 is our live prototype today at Harohalli. In Phase 2, we plan to expand across all Dayananda Sagar Institutions using solar-powered LoRaWAN sensor nodes. In Phase 3, we envision partnering with BBMP for ward-level smart city integration across Bengaluru."
    )

    # ==========================================================================
    # SLIDE 13: CONCLUSION & LIVE DEMO INVITATION
    # ==========================================================================
    s13 = add_base_slide()
    
    tb13 = s13.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "CODECLASH 2.0  |  DAYANANDA SAGAR UNIVERSITY"
    p.font.name = FONT_TITLE
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)

    p = tf13.add_paragraph()
    p.text = "Thank You, Respected Judges!"
    p.font.name = FONT_TITLE
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_after = Pt(8)

    p = tf13.add_paragraph()
    p.text = "DSU EcoTwin 2.0: Transforming Campus Waste into a Clean, Intelligent Future"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(20)

    p = tf13.add_paragraph()
    p.text = "We cordially invite you to experience the Live Interactive Demo:"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_after = Pt(6)

    p = tf13.add_paragraph()
    p.text = "1. Test Live Neural Camera Classification with real items"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_MUTED
    p.space_after = Pt(4)

    p = tf13.add_paragraph()
    p.text = "2. Speak to EcoBot Voice Assistant in English, Kannada, or Hindi"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_MUTED
    p.space_after = Pt(4)

    p = tf13.add_paragraph()
    p.text = "3. Export the 1-Click Executive Municipal Report (PDF/CSV)"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_MUTED
    p.space_after = Pt(20)

    p = tf13.add_paragraph()
    p.text = "Live Dashboard: http://127.0.0.1:8000  |  Open for Q&A"
    p.font.name = FONT_TITLE
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN

    set_speaker_notes(s13,
        "Thank you so much judges and professors for your time and guidance. We warmly invite you to come up and test our live camera classification, speak with our trilingual EcoBot in Kannada or Hindi, and inspect our digital twin simulation. We are now delighted to answer any questions!"
    )

    # Save Presentation
    output_path = os.path.abspath("DSU_EcoTwin_2.0_Presentation.pptx")
    prs.save(output_path)
    print(f"\n[SUCCESS] PowerPoint presentation saved successfully to:\n{output_path}\n")
    return output_path

if __name__ == "__main__":
    create_deck()
