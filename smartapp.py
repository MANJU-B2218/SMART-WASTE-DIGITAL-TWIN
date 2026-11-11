"""
DSU EcoTwin Smart Waste Management Digital Twin 2.0
Primary Desktop Entry Point
Dayananda Sagar University (DSU) Harohalli Campus
"""

import sys
import os

# Add dsu_ecotwin to path
current_dir = os.path.dirname(os.path.abspath(__file__))
ecotwin_dir = os.path.join(current_dir, "dsu_ecotwin")
if ecotwin_dir not in sys.path:
    sys.path.insert(0, ecotwin_dir)

try:
    from app import app
except ImportError:
    from dsu_ecotwin.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("\n" + "=" * 66)
    print("[INFO] DSU EcoTwin Smart Waste Management Digital Twin 2.0")
    print("[FEATURE 1] EcoBot Voice Assistant Pill Bar: Active")
    print("[FEATURE 2] Executive Daily Municipal Report Export: Ready")
    print(f"[SERVER] Running at: http://127.0.0.1:{port}")
    print("=" * 66 + "\n")
    app.run(host="0.0.0.0", port=port, debug=False)