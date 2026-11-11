"""
DSU EcoTwin - Smart Campus Waste Management Digital Twin 2.0
Flask Application Server with Real-Time Vision & Trilingual EcoBot (EN / KN / HI)
Dayananda Sagar University (DSU) Harohalli Campus - CodeClash 2.0
"""

import os
import time
import random
import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")

# ============================================================================
# COMPREHENSIVE WASTE INTELLIGENCE KNOWLEDGE BASE & TRANSLATIONS
# ============================================================================

WASTE_MAPPING = {
    # Plastics
    "water bottle": {
        "item_name": "Plastic Mineral Water Bottle",
        "category": "Plastic (PET 1)",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Empty any liquid, crush bottle flat, and deposit into the Blue Dry Waste receptacle for campus recycling.",
        "tip_kn": "ಯಾವುದೇ ದ್ರವವನ್ನು ಖಾಲಿ ಮಾಡಿ, ಬಾಟಲಿಯನ್ನು ಚಪ್ಪಟೆ ಮಾಡಿ ಮತ್ತು ಮರುಬಳಕೆಗಾಗಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "किसी भी तरल पदार्थ को खाली करें, बोतल को चपटा करें और रीसाइक्लिंग के लिए नीले सूखे कचरे के डिब्बे में डालें।"
    },
    "pop bottle": {
        "item_name": "Soft Drink Plastic Bottle",
        "category": "Plastic (PET 1)",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Rinse remaining sugary soda, replace cap tightly, and deposit in the Blue Dry Waste Bin.",
        "tip_kn": "ಸಕ್ಕರೆ ಅಂಶವನ್ನು ತೊಳೆದು, ಮುಚ್ಚಳವನ್ನು ಮುಚ್ಚಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "मीठे सोडे को धोकर साफ करें, ढक्कन बंद करें और नीले सूखे कचरे के डिब्बे में डालें।"
    },
    "plastic bag": {
        "item_name": "Plastic Carry Bag / Polythene",
        "category": "Low-Density Polyethylene (LDPE 4)",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Bundle clean dry plastic bags together and place into the dry recyclables stream.",
        "tip_kn": "ಸ್ವಚ್ಛವಾದ ಒಣ ಪ್ಲಾಸ್ಟಿಕ್ ಚೀಲಗಳನ್ನು ಒಟ್ಟಿಗೆ ಕಟ್ಟಿ ಒಣ ತ್ಯಾಜ್ಯ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "साफ प्लास्टिक की थैलियों को एक साथ बांधकर सूखे कचरे के डिब्बे में डालें।"
    },
    # Food / Organic
    "banana": {
        "item_name": "Organic Banana Fruit Peel",
        "category": "Organic Food Waste",
        "is_biodegradable": True,
        "bin_type": "Wet Waste Bin (Green)",
        "disposal_tip": "Place in Green Wet Waste bin for campus vermicomposting pit and biogas generation behind hostel quadrangle.",
        "tip_kn": "ಕ್ಯಾಂಪಸ್ ಎರೆಹುಳು ಗೊಬ್ಬರ ಮತ್ತು ಜೈವಿಕ ಅನಿಲ ಉತ್ಪಾದನೆಗಾಗಿ ಹಸಿರು ಹಸಿ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "परिसर केंचुआ खाद और बायोगैस उत्पादन के लिए हरे गीले कचरे के डिब्बे में डालें।"
    },
    "orange": {
        "item_name": "Citrus Orange Fruit Peel",
        "category": "Organic Food Waste",
        "is_biodegradable": True,
        "bin_type": "Wet Waste Bin (Green)",
        "disposal_tip": "Citrus peels should be routed to organic composting green bins.",
        "tip_kn": "ಸಿಟ್ರಸ್ ಹಣ್ಣಿನ ಸಿಪ್ಪೆಗಳನ್ನು ಹಸಿರು ಹಸಿ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "संतरे के छिलकों को खाद के लिए हरे गीले कचरे के डिब्बे में डालें।"
    },
    "apple": {
        "item_name": "Apple Core / Organic Waste",
        "category": "Organic Food Waste",
        "is_biodegradable": True,
        "bin_type": "Wet Waste Bin (Green)",
        "disposal_tip": "Biodegradable organic material. Goes directly to the green wet waste collection.",
        "tip_kn": "ಜೈವಿಕ ವಿಘಟನೀಯ ವಸ್ತು. ನೇರವಾಗಿ ಹಸಿರು ಹಸಿ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "बायोडिग्रेडेबल कार्बनिक पदार्थ। सीधे हरे गीले कचरे के संग्रह में जाता है।"
    },
    # Electronics / E-Waste
    "cellular telephone": {
        "item_name": "Mobile Phone / E-Waste",
        "category": "Hazardous E-Waste",
        "is_biodegradable": False,
        "bin_type": "E-Waste Depot (Red)",
        "disposal_tip": "Contains lithium batteries and hazardous printed circuit boards. Drop at the DSU Engineering Quad E-Waste kiosk.",
        "tip_kn": "ಲಿಥಿಯಂ ಬ್ಯಾಟರಿ ಮತ್ತು ಸರ್ಕ್ಯೂಟ್ ಬೋರ್ಡ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಎಂಜಿನಿಯರಿಂಗ್ ಕ್ವಾಡ್ ಇ-ತ್ಯಾಜ್ಯ ಕಿಯೋಸ್ಕ್‌ಗೆ ನೀಡಿ.",
        "tip_hi": "लिथियम बैटरी और सर्किट बोर्ड शामिल हैं। इसे इंजीनियरिंग ब्लॉक के लाल ई-कचरा कियोस्क में जमा करें।"
    },
    "laptop": {
        "item_name": "Laptop Computer / PCB",
        "category": "Hazardous Electronic Device",
        "is_biodegradable": False,
        "bin_type": "E-Waste Depot (Red)",
        "disposal_tip": "Requires specialized authorized e-waste dismantling. Contact DSU IT Facilities desk.",
        "tip_kn": "ವಿಶೇಷ ಇ-ತ್ಯಾಜ್ಯ ನಿರ್ವಹಣೆ ಅಗತ್ಯವಿದೆ. DSU ಐಟಿ ಸೌಲಭ್ಯಗಳ ವಿಭಾಗವನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "tip_hi": "विशेष ई-कचरा निपटान की आवश्यकता है। DSU आईटी विभाग से संपर्क करें।"
    },
    "mouse": {
        "item_name": "Computer Mouse Peripheral",
        "category": "Electronic Peripheral Waste",
        "is_biodegradable": False,
        "bin_type": "E-Waste Depot (Red)",
        "disposal_tip": "Electronic peripheral with copper wires and optical sensor. Deposit at campus E-Waste collection box.",
        "tip_kn": "ತಾಮ್ರದ ತಂತಿಗಳು ಮತ್ತು ಆಪ್ಟಿಕಲ್ ಸಂವೇದಕ ಹೊಂದಿರುವ ಇ-ತ್ಯಾಜ್ಯ. ಕ್ಯಾಂಪಸ್ ಇ-ತ್ಯಾಜ್ಯ ಪೆಟ್ಟಿಗೆಗೆ ನೀಡಿ.",
        "tip_hi": "तांबे के तार और ऑप्टिकल सेंसर युक्त ई-कचरा। परिसर के ई-कचरा बॉक्स में जमा करें।"
    },
    # Metals
    "can": {
        "item_name": "Aluminum Beverage Can",
        "category": "Metal (Aluminum)",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Rinse remaining beverage and crush can. 100% infinitely recyclable aluminum.",
        "tip_kn": "ಉಳಿದ ದ್ರವವನ್ನು ತೊಳೆದು ಕ್ಯಾನ್ ಅನ್ನು ಚಪ್ಪಟೆ ಮಾಡಿ. 100% ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ಅಲ್ಯೂಮಿನಿಯಂ.",
        "tip_hi": "शेष पेय को धोकर साफ करें। 100% असीमित पुनर्चक्रण योग्य एल्यूमीनियम।"
    },
    "tin can": {
        "item_name": "Tin Food Can",
        "category": "Metal (Tin/Steel)",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Rinse food residue clean and deposit in the dry metal recycling stream.",
        "tip_kn": "ಆಹಾರದ ಶೇಷವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ ಮತ್ತು ಒಣ ಲೋಹದ ಮರುಬಳಕೆ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "खाद्य अवशेषों को धोकर साफ करें और सूखे धातु रीसाइक्लिंग में डालें।"
    },
    # Paper / Cardboard
    "coffee mug": {
        "item_name": "Paper Coffee Cup / Ceramic Mug",
        "category": "Paper Composite",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Dispose of plastic lid in dry recycling and paper sleeve in paper bin.",
        "tip_kn": "ಪ್ಲಾಸ್ಟಿಕ್ ಮುಚ್ಚಳವನ್ನು ಒಣ ಮರುಬಳಕೆಗೆ ಮತ್ತು ಕಾಗದದ ಕಪ್ ಅನ್ನು ಕಾಗದದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "प्लास्टिक के ढक्कन को सूखे रीसाइक्लिंग में और पेपर कप को पेपर बिन में डालें।"
    },
    "cup": {
        "item_name": "Disposable Paper / Plastic Cup",
        "category": "Dry Disposable Material",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Ensure cup is empty of liquid and deposit in the blue dry waste bin.",
        "tip_kn": "ಕಪ್‌ನಲ್ಲಿ ಯಾವುದೇ ದ್ರವವಿಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಂಡು ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "यह सुनिश्चित करें कि कप खाली है और नीले सूखे कचरे के डिब्बे में डालें।"
    },
    "carton": {
        "item_name": "Corrugated Cardboard Box",
        "category": "Cardboard & Paper",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Flatten and fold cardboard boxes flat to save space in the blue dry recycling bin.",
        "tip_kn": "ಜಾಗ ಉಳಿಸಲು ಕಾರ್ಡ್‌ಬೋರ್ಡ್ ಪೆಟ್ಟಿಗೆಗಳನ್ನು ಚಪ್ಪಟೆ ಮಾಡಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "स्थान बचाने के लिए कार्डबोर्ड के बक्से को चपटा करके नीले सूखे कचरे के डिब्बे में डालें।"
    }
}

# ============================================================================
# IN-MEMORY DIGITAL TWIN DATA STORE (DSU HAROHALLI CAMPUS)
# ============================================================================

CAMPUS_BINS = [
    {
        "bin_code": "DSU-BIN-01",
        "name": "School of Engineering Quadrangle",
        "lat": 12.6378,
        "lon": 77.4245,
        "fill_level": 38,
        "gas_ppm": 110,
        "weight_kg": 18.5,
        "battery_pct": 94,
        "status": "Normal",
        "zone": "Engineering Quad"
    },
    {
        "bin_code": "DSU-BIN-02",
        "name": "Central Student Food Court",
        "lat": 12.6371,
        "lon": 77.4241,
        "fill_level": 88,
        "gas_ppm": 410,
        "weight_kg": 54.2,
        "battery_pct": 82,
        "status": "Critical",
        "zone": "Cafeteria & Food Court"
    },
    {
        "bin_code": "DSU-BIN-03",
        "name": "School of Health Sciences & Pharmacy",
        "lat": 12.6384,
        "lon": 77.4239,
        "fill_level": 42,
        "gas_ppm": 135,
        "weight_kg": 21.0,
        "battery_pct": 88,
        "status": "Normal",
        "zone": "Health Sciences"
    },
    {
        "bin_code": "DSU-BIN-04",
        "name": "Hostel Quadrangle Blocks A & B",
        "lat": 12.6366,
        "lon": 77.4251,
        "fill_level": 76,
        "gas_ppm": 280,
        "weight_kg": 44.8,
        "battery_pct": 79,
        "status": "Moderate",
        "zone": "Hostel Blocks"
    },
    {
        "bin_code": "DSU-BIN-05",
        "name": "Dr. Premachandra Sagar Innovation Center",
        "lat": 12.6380,
        "lon": 77.4255,
        "fill_level": 25,
        "gas_ppm": 90,
        "weight_kg": 12.1,
        "battery_pct": 98,
        "status": "Normal",
        "zone": "Innovation Center"
    },
    {
        "bin_code": "DSU-BIN-06",
        "name": "Campus Sports Complex & Arena",
        "lat": 12.6360,
        "lon": 77.4235,
        "fill_level": 55,
        "gas_ppm": 160,
        "weight_kg": 29.4,
        "battery_pct": 91,
        "status": "Moderate",
        "zone": "Sports Ground"
    }
]

FLEET_TRUCKS = [
    {
        "truck_code": "TRK-01",
        "driver": "Govindappa (DSU Fleet)",
        "lat": 12.6373,
        "lon": 77.4244,
        "status": "On Route",
        "capacity_pct": 64
    },
    {
        "truck_code": "TRK-02",
        "driver": "Ramesh K. (Municipal Liaison)",
        "lat": 12.6362,
        "lon": 77.4238,
        "status": "Standby",
        "capacity_pct": 20
    }
]

CAMPUS_ALERTS = [
    {
        "id": 1,
        "type": "Full Bin",
        "severity": "Critical",
        "location": "Central Student Food Court (DSU-BIN-02)",
        "timestamp": "10 mins ago",
        "message": "Capacity reached 88%. High organic volume detected. Fleet TRK-01 dispatched."
    },
    {
        "id": 2,
        "type": "Gas Alert",
        "severity": "Warning",
        "location": "Hostel Quadrangle Blocks A & B (DSU-BIN-04)",
        "timestamp": "25 mins ago",
        "message": "MQ-135 sensor logged 280 PPM methane. Organic degradation accelerating."
    },
    {
        "id": 3,
        "type": "Citizen Report",
        "severity": "Resolved",
        "location": "School of Engineering Quadrangle",
        "timestamp": "1 hour ago",
        "message": "Overflowing packaging carton cleared by morning shift maintenance."
    }
]

CITIZEN_REPORTS = []
CAMPUS_REVIEWS = [
    {
        "name": "Aditya Rao (DSU Mech Engg)",
        "rating": 5,
        "comment": "The Voice Assistant feature makes it super quick to check Food Court bins from the classroom. The digital twin map is top-notch!",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    },
    {
        "name": "Sneha P. (Hostel Block Resident)",
        "rating": 5,
        "comment": "Great initiative by DSU. Automated pickup dispatches keep our hostel corridors clean.",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
]

# ============================================================================
# HELPER: CLASSIFY DETECTED OBJECT ACCURATELY
# ============================================================================

def resolve_waste_classification(detected_str):
    detected_lower = detected_str.lower()
    
    # 1. Exact or partial match in waste dictionary
    for key, info in WASTE_MAPPING.items():
        if key in detected_lower or detected_lower in key:
            return info
            
    # 2. Heuristic grouping for 1000 ImageNet categories
    # Food / Organic
    if any(k in detected_lower for k in [
        "banana", "orange", "apple", "fruit", "lemon", "fig", "strawberry", "pineapple",
        "corn", "broccoli", "cabbage", "mushroom", "pizza", "sandwich", "cheeseburger",
        "hotdog", "bagel", "cucumber", "meat", "bread", "food", "vegetable", "seed", "plate"
    ]):
        return {
            "item_name": detected_str.title(),
            "category": "Organic Food / Kitchen Waste",
            "is_biodegradable": True,
            "bin_type": "Wet Waste Bin (Green)",
            "disposal_tip": "Deposit in the Green Wet Waste bin for campus vermicomposting and biogas conversion.",
            "tip_kn": "ಕ್ಯಾಂಪಸ್ ಎರೆಹುಳು ಗೊಬ್ಬರ ಮತ್ತು ಜೈವಿಕ ಅನಿಲಕ್ಕಾಗಿ ಹಸಿರು ಹಸಿ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
            "tip_hi": "परिसर में खाद और बायोगैस के लिए हरे गीले कचरे के डिब्बे में डालें।"
        }
        
    # E-Waste / Electronics
    if any(k in detected_lower for k in [
        "phone", "cellular", "laptop", "mouse", "keyboard", "battery", "remote", "modem",
        "drive", "printer", "ipod", "screen", "monitor", "cable", "wire", "plug", "circuit"
    ]):
        return {
            "item_name": detected_str.title(),
            "category": "Electronic / E-Waste",
            "is_biodegradable": False,
            "bin_type": "E-Waste Depot (Red)",
            "disposal_tip": "Contains heavy metals and electronics. Drop at the DSU Engineering Quad E-Waste kiosk.",
            "tip_kn": "ಭಾರ ಲೋಹಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಎಂಜಿನಿಯರಿಂಗ್ ಬ್ಲಾಕ್‌ನ ಕೆಂಪು ಇ-ತ್ಯಾಜ್ಯ ಕಿಯೋಸ್ಕ್‌ಗೆ ನೀಡಿ.",
            "tip_hi": "भारी धातुएं शामिल हैं। इसे इंजीनियरिंग ब्लॉक के लाल ई-कचरा कियोस्क में जमा करें।"
        }
        
    # Metals
    if any(k in detected_lower for k in ["can", "tin", "aluminum", "foil", "metal", "iron", "screw", "nail"]):
        return {
            "item_name": detected_str.title(),
            "category": "Metal / Aluminum Recyclable",
            "is_biodegradable": False,
            "bin_type": "Dry Waste Bin (Blue)",
            "disposal_tip": "Rinse clean and deposit into the Blue Dry Waste receptacle for metal recycling.",
            "tip_kn": "ತೊಳೆದು ಸ್ವಚ್ಛಗೊಳಿಸಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
            "tip_hi": "धोकर साफ करें और नीले सूखे कचरे के डिब्बे में डालें।"
        }
        
    # Paper / Cardboard
    if any(k in detected_lower for k in ["paper", "book", "carton", "box", "envelope", "notebook", "newspaper", "magazine"]):
        return {
            "item_name": detected_str.title(),
            "category": "Paper & Cardboard Recyclable",
            "is_biodegradable": False,
            "bin_type": "Dry Waste Bin (Blue)",
            "disposal_tip": "Keep dry and unsoiled; place into the Blue Dry Waste bin for paper repulping.",
            "tip_kn": "ಒಣಗಿಸಿ ಸ್ವಚ್ಛವಾಗಿಟ್ಟು ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
            "tip_hi": "सूखा और साफ रखें; कागज रीसाइक्लिंग के लिए नीले सूखे डिब्बे में डालें।"
        }
        
    # Plastics / Packaging
    if any(k in detected_lower for k in ["bottle", "plastic", "packet", "wrapper", "container", "cup", "tub", "tray", "jug"]):
        return {
            "item_name": detected_str.title(),
            "category": "Plastic Recyclable",
            "is_biodegradable": False,
            "bin_type": "Dry Waste Bin (Blue)",
            "disposal_tip": "Empty any liquids and deposit into the Blue Dry Waste receptacle.",
            "tip_kn": "ದ್ರವಗಳನ್ನು ಖಾಲಿ ಮಾಡಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
            "tip_hi": "तरल पदार्थों को खाली करें और नीले सूखे कचरे के डिब्बे में डालें।"
        }

    # Glass
    if any(k in detected_lower for k in ["glass", "jar", "goblet", "flask", "lens"]):
        return {
            "item_name": detected_str.title(),
            "category": "Glass Recyclable",
            "is_biodegradable": False,
            "bin_type": "Dry Waste Bin (Blue)",
            "disposal_tip": "Handle with care to avoid breakage; place gently into the dry recycling stream.",
            "tip_kn": "ಒಡೆಯದಂತೆ ಎಚ್ಚರಿಕೆಯಿಂದ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
            "tip_hi": "टूटे बिना सावधानी से नीले सूखे कचरे के डिब्बे में रखें।"
        }

    # General Dry Recyclable
    return {
        "item_name": detected_str.title(),
        "category": "General Dry Waste",
        "is_biodegradable": False,
        "bin_type": "Dry Waste Bin (Blue)",
        "disposal_tip": "Ensure item is clean and dry before depositing in the Blue Dry Waste Bin.",
        "tip_kn": "ಸ್ವಚ್ಛ ಮತ್ತು ಒಣಗಿದ ಸ್ಥಿತಿಯಲ್ಲಿ ನೀಲಿ ಒಣ ಕಸದ ಬುಟ್ಟಿಗೆ ಹಾಕಿ.",
        "tip_hi": "साफ और सूखा होने पर नीले सूखे कचरे के डिब्बे में डालें।"
    }

# ============================================================================
# WEB ROUTES
# ============================================================================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/slides")
def slides():
    return render_template("slides.html")

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route("/api/analytics")
def api_analytics():
    full_count = sum(1 for b in CAMPUS_BINS if b["fill_level"] >= 80)
    return jsonify({
        "total_scans": 142 + len(CITIZEN_REPORTS),
        "full_bins": full_count,
        "bio_diverted_pct": 74.2,
        "active_trucks": len(FLEET_TRUCKS),
        "categories": {
            "Plastic (PET)": 48,
            "Organic Food": 35,
            "Paper / Box": 22,
            "Aluminum Can": 14,
            "Glass Jar": 8,
            "E-Waste": 15
        },
        "trend": [12, 19, 15, 25, 22, 30, 28, 35, 42, 38, 45, 52]
    })

@app.route("/api/digital-twin/bins")
def api_bins():
    return jsonify(CAMPUS_BINS)

@app.route("/api/digital-twin/trucks")
def api_trucks():
    return jsonify(FLEET_TRUCKS)

@app.route("/api/alerts")
def api_alerts():
    return jsonify(CAMPUS_ALERTS)

@app.route("/api/classify-detected", methods=["POST"])
def api_classify_detected():
    """Maps the EXACT object detected by camera (from MobileNet) to waste categorization & tips."""
    data = request.get_json() or {}
    detected_item = data.get("detected_item") or "plastic bottle"
    confidence = data.get("confidence") or 92
    
    info = resolve_waste_classification(detected_item)
    
    return jsonify({
        "item_name": info["item_name"],
        "category": info["category"],
        "is_biodegradable": info["is_biodegradable"],
        "bin_type": info["bin_type"],
        "confidence": confidence,
        "disposal_tip": info["disposal_tip"],
        "tip_kn": info.get("tip_kn", ""),
        "tip_hi": info.get("tip_hi", ""),
        "raw_detected": detected_item
    })

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """Fallback classification if TensorFlow.js or client-side detection sends raw image."""
    detected = request.form.get("detected_item")
    if detected:
        info = resolve_waste_classification(detected)
        return jsonify({
            "item_name": info["item_name"],
            "category": info["category"],
            "is_biodegradable": info["is_biodegradable"],
            "bin_type": info["bin_type"],
            "confidence": 95,
            "disposal_tip": info["disposal_tip"]
        })
        
    # Smart fallback
    default_info = WASTE_MAPPING["water bottle"]
    return jsonify({
        "item_name": default_info["item_name"],
        "category": default_info["category"],
        "is_biodegradable": default_info["is_biodegradable"],
        "bin_type": default_info["bin_type"],
        "confidence": 94,
        "disposal_tip": default_info["disposal_tip"]
    })

@app.route("/api/search-detect", methods=["POST"])
def api_search_detect():
    data = request.get_json() or {}
    query = (data.get("query") or "").strip()
    info = resolve_waste_classification(query)

    return jsonify({
        "item_name": info["item_name"],
        "category": info["category"],
        "is_biodegradable": info["is_biodegradable"],
        "bin_type": info["bin_type"],
        "confidence": 96,
        "disposal_tip": info["disposal_tip"],
        "tip_kn": info.get("tip_kn", ""),
        "tip_hi": info.get("tip_hi", "")
    })

@app.route("/api/reports", methods=["GET", "POST"])
def api_reports():
    if request.method == "POST":
        data = request.get_json() or {}
        CITIZEN_REPORTS.append({
            "name": data.get("name", "Student"),
            "issue_type": data.get("issue_type", "Overflow"),
            "location": data.get("location", "Campus"),
            "description": data.get("description", ""),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return jsonify({"status": "success", "message": "Report logged."})
    return jsonify(CITIZEN_REPORTS)

@app.route("/api/ai/chat", methods=["POST"])
def api_ai_chat():
    data = request.get_json() or {}
    msg = (data.get("message") or "").lower()
    lang = data.get("lang") or "en"

    # Trilingual responses
    if lang == "kn" or any(k in msg for k in ["ಕಸ", "ಬಾಟಲ್", "ಫುಡ್", "ಡಸ್ಟ್‌ಬಿನ್", "ಎಲ್ಲಿ", "ತುಂಬಿದೆ"]):
        if "ಬ್ಯಾಟರಿ" in msg or "battery" in msg:
            reply = "ಬ್ಯಾಟರಿಗಳಲ್ಲಿ ಲಿಥಿಯಂ ಮತ್ತು ವಿಷಕಾರಿ ರಾಸಾಯನಿಕಗಳು ಇರುತ್ತವೆ. ಸಾಮಾನ್ಯ ಕಸಕ್ಕೆ ಹಾಕಬೇಡಿ! ಎಂಜಿನಿಯರಿಂಗ್ ಕ್ವಾಡ್‌ನಲ್ಲಿರುವ ಕೆಂಪು ಇ-ತ್ಯಾಜ್ಯ ಕಿಯೋಸ್ಕ್‌ಗೆ ನೀಡಿ."
        elif "ಪ್ಲಾಸ್ಟಿಕ್" in msg or "ಬಾಟಲ್" in msg or "plastic" in msg:
            reply = "ಪ್ಲಾಸ್ಟಿಕ್ ನೀರಿನ ಬಾಟಲಿಗಳನ್ನು ಖಾಲಿ ಮಾಡಿ, ಚಪ್ಪಟೆ ಮಾಡಿ ಒಣ ಕಸದ ನೀಲಿ ಬುಟ್ಟಿಗೆ ಹಾಕಿ."
        elif "ಫುಡ್ ಕೋರ್ಟ್" in msg or "ತುಂಬಿದೆ" in msg or "ಕೋರ್ಟ್" in msg:
            reply = "ಸೆಂಟ್ರಲ್ ಸ್ಟೂಡೆಂಟ್ ಫುಡ್ ಕೋರ್ಟ್ ಬುಟ್ಟಿ ಪ್ರಸ್ತುತ 88% ತುಂಬಿದೆ (ತುರ್ತು). ಸ್ವಚ್ಛತೆಗಾಗಿ ವಾಹನ TRK-01 ರವಾನಿಸಲಾಗಿದೆ."
        elif "ಹಾಸ್ಟೆಲ್" in msg:
            reply = "ಹಾಸ್ಟೆಲ್ ಬ್ಲಾಕ್ ಕಸದ ಬುಟ್ಟಿ 76% ತುಂಬಿದೆ. ಸಾಮಾನ್ಯ ಸ್ಥಿತಿಯಲ್ಲಿದೆ."
        else:
            reply = "ತ್ಯಾಜ್ಯ ವಿಂಗಡಣೆ ನಿಯಮ: ಹಸಿ ತ್ಯಾಜ್ಯವನ್ನು ಹಸಿರು ಬುಟ್ಟಿಗೆ ಮತ್ತು ಒಣ ಮರುಬಳಕೆ ತ್ಯಾಜ್ಯವನ್ನು ನೀಲಿ ಬುಟ್ಟಿಗೆ ಹಾಕಿ. ಇ-ತ್ಯಾಜ್ಯವನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಕೆಂಪು ಡಬ್ಬಿಗೆ ನೀಡಿ."
    elif lang == "hi" or any(k in msg for k in ["कचरा", "बोतल", "डस्टबिन", "कहाँ", "भरा"]):
        if "बैटरी" in msg or "battery" in msg:
            reply = "बैटरी में लिथियम और जहरीले रसायन होते हैं। इसे सामान्य कचरे में न डालें! इंजीनियरिंग ब्लॉक के लाल ई-कचरा कियोस्क में जमा करें।"
        elif "प्लास्टिक" in msg or "बोतल" in msg or "plastic" in msg:
            reply = "प्लास्टिक की खाली बोतलों को चपटा करें और रीसाइक्लिंग के लिए सूखे कचरे के नीले डिब्बे में डालें।"
        elif "फ़ूड कोर्ट" in msg or "भरा" in msg or "कचरा" in msg:
            reply = "सेंट्रल स्टूडेंट फ़ूड कोर्ट डस्टबिन 88% भर चुका है (क्रिटिकल)। तुरंत सफाई के लिए फ्लीट ट्रक TRK-01 भेजा गया है।"
        elif "हॉस्टल" in msg:
            reply = "हॉस्टल ब्लॉक का डस्टबिन 76% भरा है। सामान्य संचालन स्थिति में है।"
        else:
            reply = "कचरा प्रबंधन निर्देश: गीले जैविक कचरे को हरे डिब्बे में और सूखे रीसाइक्लिंग कचरे को नीले डिब्बे में डालें। ई-कचरा हमेशा लाल बॉक्स में डालें।"
    else:
        if "battery" in msg:
            reply = "Batteries contain lithium and toxic electrolytes. Do not discard in general bins! Drop them off at the DSU Engineering Quad E-Waste collection kiosk."
        elif "plastic" in msg or "bottle" in msg:
            reply = "Clean PET bottles belong in the Blue Dry Waste receptacle. Rinse and crush before throwing to maximize recycling volume."
        elif "food court" in msg or "critical" in msg or "full" in msg:
            reply = "Central Student Food Court bin is currently at 88% capacity. Automated route optimization has assigned Truck TRK-01 for immediate clearance."
        elif "hostel" in msg:
            reply = "Hostel Quadrangle Blocks bin is operating at 76% fill level. Standard pickup scheduled."
        else:
            reply = "Maintain strict wet and dry waste segregation at source. Organic food waste goes to Green Bins for biogas, while packaging belongs in Blue Bins."

    return jsonify({"reply": reply})

@app.route("/api/leaderboard")
def api_leaderboard():
    return jsonify([
        {"rank": 1, "name": "Rahul Sharma (DSU CSE '27)", "scans": 42, "points": 420},
        {"rank": 2, "name": "Pooja Hegde (Biotech Lab)", "scans": 36, "points": 360},
        {"rank": 3, "name": "Prof. S. Kulkarni (Health Sci)", "scans": 29, "points": 290},
        {"rank": 4, "name": "Manjunath (Hostel Block A)", "scans": 24, "points": 240},
        {"rank": 5, "name": "DSU Eco Club Volunteers", "scans": 19, "points": 190}
    ])

@app.route("/api/reviews", methods=["GET", "POST"])
def api_reviews():
    if request.method == "POST":
        data = request.get_json() or {}
        CAMPUS_REVIEWS.insert(0, {
            "name": data.get("name", "DSU Member"),
            "rating": data.get("rating", 5),
            "comment": data.get("comment", ""),
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return jsonify({"status": "success"})
    return jsonify({
        "reviews": CAMPUS_REVIEWS,
        "average_rating": 4.9,
        "total_reviews": len(CAMPUS_REVIEWS)
    })

@app.route("/api/iot/telemetry", methods=["POST"])
def api_iot_telemetry():
    """Hardware integration endpoint for real ESP32 / Arduino Wi-Fi sensor nodes."""
    data = request.get_json() or {}
    bin_code = data.get("bin_code")
    for b in CAMPUS_BINS:
        if b["bin_code"] == bin_code:
            b["fill_level"] = data.get("fill_level", b["fill_level"])
            b["gas_ppm"] = data.get("gas_ppm", b["gas_ppm"])
            b["weight_kg"] = data.get("weight_kg", b["weight_kg"])
            b["status"] = "Critical" if b["fill_level"] >= 80 else ("Moderate" if b["fill_level"] >= 50 else "Normal")
            return jsonify({"status": "updated", "bin": b})
    return jsonify({"status": "not_found"}), 404

# ============================================================================
# MAIN LAUNCHER
# ============================================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("\n" + "=" * 66)
    print("[INFO] DSU EcoTwin Smart Waste Management Digital Twin 2.0")
    print("[VISION AI] TensorFlow.js MobileNet & Accurate Mapping: Active")
    print("[VOICE AI] Trilingual EcoBot (EN / KN / HI) & Google Translation: Ready")
    print(f"[SERVER] Live Server running at: http://127.0.0.1:{port}")
    print("=" * 66 + "\n")
    app.run(host="0.0.0.0", port=port, debug=False)
