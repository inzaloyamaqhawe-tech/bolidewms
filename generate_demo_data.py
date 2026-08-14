"""
DSA Warehouse & Production Management System - DEMO DATA GENERATOR
=====================================================================
Generates a self-contained, internally-consistent demo dataset that mirrors
the shape of data the real backend (vvd.py, NOT modified) reads out of
SQL Server (ItemTrack / MOTrack databases) and hands to the frontend
(dsav0011.html).

This script does NOT touch vvd.py or dsav0011.html. It only writes
`demo_data_seed.json` inside this `demo/` folder. `demo_server.py` loads
that seed (or the mutable `demo_data.json` if it already exists) and serves
it over HTTP with the same URL paths/response shapes the frontend expects.

Run:  python generate_demo_data.py
"""
import json
import random
from datetime import datetime, timedelta

random.seed(42)

TODAY = datetime(2026, 8, 11, 9, 0, 0)

OUT_SEED = "demo_data_seed.json"

# ---------------------------------------------------------------------------
# 1. LOGIN USERS (MOTrack.dbo.Users) - the 4 requested logins + a couple extra
# ---------------------------------------------------------------------------
USERS = [
    {"id": 1, "name": "LANGA", "surname": "Ngidi", "email": "langa@dsawarehouse.demo",
     "password": "DSA100%", "role": "admin", "position": "Warehouse Admin", "is_active": True},
    {"id": 2, "name": "SIZWE", "surname": "Dube", "email": "sizwe@dsawarehouse.demo",
     "password": "DSA200%", "role": "dsaprod", "position": "DSA Production User", "is_active": True},
    {"id": 3, "name": "SAM", "surname": "Khumalo", "email": "sam@dsawarehouse.demo",
     "password": "DSA300%", "role": "management", "position": "Operations Management", "is_active": True},
    {"id": 4, "name": "DANI", "surname": "Nkosi", "email": "dani@dsawarehouse.demo",
     "password": "DSA400%", "role": "warehouse", "position": "Warehouse User", "is_active": True},
]

# ---------------------------------------------------------------------------
# 2. WORKSTATIONS (MOTrack.dbo.workstations) - the 9-stage production line
# ---------------------------------------------------------------------------
WORKSTATION_NAMES = ["Cut", "In Prep", "Glue", "Build", "Scribe", "Polishing",
                     "Scope", "Measurement", "Packaging"]
WORKSTATIONS = [
    {"id": i + 1, "name": name, "description": f"{name} stage", "is_active": True,
     "display_order": i + 1, "created_at": (TODAY - timedelta(days=400)).isoformat()}
    for i, name in enumerate(WORKSTATION_NAMES)
]

# ---------------------------------------------------------------------------
# 3. PRODUCTION FLOOR WORKERS (MOTrack.dbo.Production_Users)
# ---------------------------------------------------------------------------
WORKER_NAMES = [
    ("Sammy", "Mahapia"), ("Albert", "Malebana"), ("Calrick", "Myers"), ("Anna", "Kekana"),
    ("Falies", "Mashigo"), ("Greatfull", "Sithole"), ("Karabo", "Manganyi"), ("Lindiwe", "Mashilo"),
    ("Maria", "Thopola"), ("Martha", "Mtshweni"), ("Sandra", "Chauke"), ("Sibusiso", "Mpatlanyane"),
    ("Thuso", "Manganyi"), ("Rochelle", "Van Rooyen"), ("Cathrine", "Vilakazi"), ("Florah", "Dlamini"),
    ("Willie", "Ledwaba"), ("Princess", "Skosana"), ("Bonte", "Mokoena"), ("Petunia", "Radebe"),
    ("Freddy", "Maluleke"), ("Palesa", "Letsoalo"), ("Motlapule", "Tau"), ("Given", "Zulu"),
    ("Nomsa", "Mahlangu"), ("Elias", "Ndlovu"), ("Zanele", "Cele"), ("Tumelo", "Mokoena"),
]

def make_username(first, surname):
    return first + surname.split(" ")[0][0].upper() + surname.split(" ")[0][1:2].lower()

PRODUCTION_USERS = []
for i, (first, surname) in enumerate(WORKER_NAMES):
    ws = WORKSTATIONS[i % len(WORKSTATIONS)]
    PRODUCTION_USERS.append({
        "id": i + 1,
        "employee_username": make_username(first, surname),
        "full_name": f"{first} {surname}",
        "Name": first,
        "Surname": surname,
        "Position": "Production Operator",
        "Role": "employee",
        "is_active": True,
        "workstation_id": ws["id"],
        "multi_workstation_ids": None,
    })

# ---------------------------------------------------------------------------
# 4. MATERIAL CATALOG (ItemTrack.dbo.ic_Item) - fibre / RF cable assembly BOM
# ---------------------------------------------------------------------------
MATERIALS = [
    {"item_number": "FO-CONN-SC-APC", "description": "SC/APC Fibre Connector", "uom": "EA"},
    {"item_number": "FO-CONN-LC-UPC", "description": "LC/UPC Fibre Connector", "uom": "EA"},
    {"item_number": "FO-PIGTAIL-SM", "description": "Single-Mode Fibre Pigtail 1.5m", "uom": "EA"},
    {"item_number": "FO-CABLE-SM-2C", "description": "Single-Mode Fibre Cable 2-Core", "uom": "M"},
    {"item_number": "FO-CABLE-SM-4C", "description": "Single-Mode Fibre Cable 4-Core", "uom": "M"},
    {"item_number": "FO-SPLITTER-1X8", "description": "1x8 PLC Fibre Splitter", "uom": "EA"},
    {"item_number": "FO-SPLITTER-1X16", "description": "1x16 PLC Fibre Splitter", "uom": "EA"},
    {"item_number": "FO-PATCHPANEL-24", "description": "24-Port Fibre Patch Panel", "uom": "EA"},
    {"item_number": "FO-SPLICE-TRAY", "description": "Fibre Splice Tray", "uom": "EA"},
    {"item_number": "FO-HEATSHRINK-45", "description": "45mm Fibre Splice Protector Heat Shrink", "uom": "EA"},
    {"item_number": "RF-CONN-N-MALE", "description": "N-Type Male RF Connector", "uom": "EA"},
    {"item_number": "RF-CONN-N-FEMALE", "description": "N-Type Female RF Connector", "uom": "EA"},
    {"item_number": "RF-CONN-SMA-MALE", "description": "SMA Male RF Connector", "uom": "EA"},
    {"item_number": "RF-CABLE-LMR400", "description": "LMR-400 RF Coaxial Cable", "uom": "M"},
    {"item_number": "RF-CABLE-LMR240", "description": "LMR-240 RF Coaxial Cable", "uom": "M"},
    {"item_number": "RF-BOOT-WEATHERPROOF", "description": "Weatherproof Connector Boot", "uom": "EA"},
    {"item_number": "RF-GROUNDING-KIT", "description": "Coax Grounding Kit", "uom": "EA"},
    {"item_number": "CRIMP-FERRULE-STD", "description": "Standard Crimp Ferrule", "uom": "EA"},
    {"item_number": "CABLE-TIE-200MM", "description": "200mm Cable Tie", "uom": "EA"},
    {"item_number": "HEATSHRINK-TUBE-12MM", "description": "12mm Heat Shrink Tube", "uom": "M"},
    {"item_number": "LABEL-CABLE-WRAP", "description": "Cable Wrap Label", "uom": "EA"},
    {"item_number": "FTTA-JUMPER-2M", "description": "FTTA Fibre Jumper 2m", "uom": "EA"},
    {"item_number": "FTTA-BREAKOUT-KIT", "description": "FTTA Breakout Kit", "uom": "EA"},
    {"item_number": "ARMOUR-TAPE", "description": "Armoured Cable Tape", "uom": "M"},
    {"item_number": "SILICA-GEL-PACK", "description": "Silica Gel Desiccant Pack", "uom": "EA"},
    {"item_number": "CABLE-GLAND-M20", "description": "M20 Cable Gland", "uom": "EA"},
    {"item_number": "PATCH-CORD-SC-1M", "description": "SC-SC Patch Cord 1m", "uom": "EA"},
]
for i, m in enumerate(MATERIALS):
    m["ici_id"] = 5000 + i
    m["min_qty"] = random.choice([50, 100, 150, 200])
    m["reorder_qty"] = random.choice([200, 300, 500])

MATERIAL_BY_ITEM = {m["item_number"]: m for m in MATERIALS}

ASSEMBLY_BOM = {
    "Universal Assembly FO": ["FO-CONN-SC-APC", "FO-CONN-LC-UPC", "FO-PIGTAIL-SM", "FO-CABLE-SM-2C",
                              "FO-HEATSHRINK-45", "CABLE-TIE-200MM", "LABEL-CABLE-WRAP"],
    "FO Splitter": ["FO-SPLITTER-1X8", "FO-SPLITTER-1X16", "FO-SPLICE-TRAY", "FO-PIGTAIL-SM",
                    "FO-HEATSHRINK-45", "LABEL-CABLE-WRAP"],
    "RF Cable Assembly": ["RF-CONN-N-MALE", "RF-CONN-N-FEMALE", "RF-CONN-SMA-MALE", "RF-CABLE-LMR400",
                          "RF-CABLE-LMR240", "RF-BOOT-WEATHERPROOF", "RF-GROUNDING-KIT", "CRIMP-FERRULE-STD"],
    "FO Cable Assembly FTTA": ["FTTA-JUMPER-2M", "FTTA-BREAKOUT-KIT", "ARMOUR-TAPE", "CABLE-GLAND-M20",
                               "SILICA-GEL-PACK", "CABLE-TIE-200MM"],
    "FO Patch Panel": ["FO-PATCHPANEL-24", "PATCH-CORD-SC-1M", "FO-SPLICE-TRAY", "LABEL-CABLE-WRAP",
                       "FO-HEATSHRINK-45"],
    "N/A": ["CABLE-TIE-200MM", "LABEL-CABLE-WRAP", "HEATSHRINK-TUBE-12MM"],
}

CUSTOMERS = [
    ("MCT01", "MCT TELECOMMUNICATIONS (PTY) LTD"),
    ("MCT02", "M C T TELECOMMUNICATIONS (PTY) LTD"),
    ("UNKDEB", "UNKNOWN DEBTOR (ZAR - COD)"),
    ("ALARIS", "ALARIS ANTENNAS (PTY) LTD"),
    ("VODA01", "VODACOM (PTY) LTD"),
    ("THALES", "THALES AEROSPACE COMMUNICATIONS CAPE TOWN (PTY) LTD"),
    ("DARKFI", "DARK FIBRE AFRICA (PTY) LTD"),
    ("REUTEC", "REUTECH RADAR SYSTEMS, A DIV OF REUTECH (PTY) LTD"),
    ("MTN01", "MTN SOUTH AFRICA (PTY) LTD"),
    ("TELKOM", "TELKOM SA SOC LTD"),
]

ASSEMBLY_TYPES = list(ASSEMBLY_BOM.keys())

STATUS_ID_MAP = {
    129: "New MO", 168: "Released", 154: "Printed", 185: "Started",
    86: "Issued", 200: "Transferred", 220: "Completed", 24: "Closed",
}
STATUS_TEXT_TO_ID = {v: k for k, v in STATUS_ID_MAP.items()}

ADMIN_EMAILS = {
    "admin": "langa@dsawarehouse.demo",
    "dsaprod": "sizwe@dsawarehouse.demo",
    "management": "sam@dsawarehouse.demo",
    "warehouse": "dani@dsawarehouse.demo",
}


def iso(dt):
    return dt.isoformat()


# ---------------------------------------------------------------------------
# 5. MANUFACTURING ORDERS (mr_Mo_Header / vw_Mo_Header_Select) + BOM lines
# ---------------------------------------------------------------------------
MOS = []
MO_MATERIAL = []
MO_LINE = []
MO_TRANSFER = []
STATUS_EVENTS = []
MO_ASSIGNMENTS = []
MO_COMMENTS = []
WORKSTATION_COMPLETIONS = []
REPORTS = []

NUM_MOS = 58
mom_id_seq = 1
mol_id_seq = 1
transfer_id_seq = 1
event_id_seq = 1
assignment_id_seq = 1
comment_id_seq = 1
completion_id_seq = 1
report_id_seq = 1

# Weighted lifecycle stages so the dashboard tells a believable story
LIFECYCLE_WEIGHTS = [
    ("new", 8), ("started", 10), ("partial_issue", 12), ("issued", 10),
    ("partial_transfer", 8), ("transferred", 6), ("completed", 4),
]
LIFECYCLE_POOL = [s for s, w in LIFECYCLE_WEIGHTS for _ in range(w)]

# The random due_offset_days ranges below only reach back ~40 days from TODAY,
# so May/June 2026 (both 2-3+ months before TODAY) would otherwise have zero
# MOs - which starves any "by due month" report/chart of demo data for those
# months. Pin a handful of MOs to explicit May/June dates so those months
# always have something to show (they're finished jobs by now, hence
# completed/transferred).
EXTRA_DUE_DATE_OVERRIDES = {
    58: {"date_required": datetime(2026, 5, 14, 9, 0, 0), "stage": "completed"},
    59: {"date_required": datetime(2026, 6, 3, 9, 0, 0), "stage": "transferred"},
    60: {"date_required": datetime(2026, 6, 16, 9, 0, 0), "stage": "completed"},
    61: {"date_required": datetime(2026, 6, 27, 9, 0, 0), "stage": "completed"},
}
NUM_MOS = max(NUM_MOS, max(EXTRA_DUE_DATE_OVERRIDES) + 1)

for i in range(NUM_MOS):
    moh_id = 172001 + i
    mo_number = f"MO01726{45 + i:02d}" if i < 55 else f"MO01727{i-54:02d}"
    customer_code, customer_name = random.choice(CUSTOMERS)
    assembly_type = random.choices(
        ASSEMBLY_TYPES, weights=[28, 16, 26, 14, 12, 4], k=1
    )[0]
    qty = random.choice([12, 20, 24, 36, 50, 60, 75, 90, 120, 150, 200, 219, 263, 438, 690])

    override = EXTRA_DUE_DATE_OVERRIDES.get(i)
    if override:
        stage = override["stage"]
        date_required = override["date_required"]
    else:
        # Pick lifecycle stage FIRST so due/creation dates stay internally
        # consistent (a "Completed"/"Transferred" job can't finish in the future).
        stage = random.choice(LIFECYCLE_POOL)

        if stage == "completed":
            due_offset_days = random.randint(-40, -2)
        elif stage in ("transferred", "partial_transfer"):
            due_offset_days = random.randint(-30, 20)
        elif stage == "issued":
            due_offset_days = random.randint(-15, 60)
        elif stage == "partial_issue":
            due_offset_days = random.randint(-5, 90)
        else:  # new / started - can be due any time, mostly future
            due_offset_days = random.choice(list(range(-20, -1)) + list(range(0, 130)))
        date_required = TODAY + timedelta(days=due_offset_days)

    # Creation date: 10-70 days before due date, always in the past
    created_offset = random.randint(10, 70)
    datetime_create = date_required - timedelta(days=created_offset)
    if datetime_create > TODAY - timedelta(days=1):
        datetime_create = TODAY - timedelta(days=random.randint(1, 5))

    is_priority = 1 if random.random() < 0.12 else 0

    item_number_1 = f"ASM-{assembly_type[:2].upper()}-{1000 + i}"
    item_description_1 = f"{assembly_type} Assembly - {customer_name.split(' ')[0].title()}"

    mo = {
        "moh_id": moh_id,
        "mo_number": mo_number,
        "boh_ID": 9000 + (i % 12),
        "qty": qty,
        "date_required": iso(date_required),
        "datetime_create": iso(datetime_create),
        "oe_customer": customer_code,
        "oe_customer_name": customer_name,
        "oe_ordnumber": f"SO{100000 + i}",
        "assembly_type": assembly_type,
        "item_number_1": item_number_1,
        "item_description_1": item_description_1,
        "revision_1": random.choice(["A", "B", "C", "1", "2"]),
        "released_by": random.choice(["LANGA", "DANI", "SYSTEM"]),
        "notes": None,
        "on_hold": 0,
        "on_hold_reason": None,
        "is_priority": is_priority,
        "_stage": stage,
    }
    MOS.append(mo)

    # ---- BOM / material lines -------------------------------------------------
    bom_items = ASSEMBLY_BOM[assembly_type]
    num_lines = random.randint(min(3, len(bom_items)), min(7, len(bom_items)))
    chosen_items = random.sample(bom_items, num_lines)

    # Overall pick fraction driven by lifecycle stage
    pick_fraction = {
        "new": 0.0, "started": 0.0, "partial_issue": random.uniform(0.15, 0.85),
        "issued": 1.0, "partial_transfer": 1.0, "transferred": 1.0, "completed": 1.0,
    }[stage]

    total_required = 0.0
    total_issued = 0.0
    for line_no, item_number in enumerate(chosen_items, start=1):
        mat = MATERIAL_BY_ITEM[item_number]
        per_unit = round(random.uniform(0.5, 3.0), 2) if mat["uom"] == "EA" else round(random.uniform(0.3, 2.5), 2)
        qty_required = round(qty * per_unit, 2)
        # No noise for MOs that haven't started picking yet - a "New MO" must
        # show 0 issued on every line, not a random sliver from variance.
        variance = random.uniform(-0.08, 0.08) if pick_fraction > 0 else 0.0
        line_pick_fraction = max(0.0, min(1.0, pick_fraction + variance))
        qty_issued = round(qty_required * line_pick_fraction, 2)
        qty_scrap = round(qty_issued * random.uniform(0, 0.03), 2) if qty_issued > 0 else 0.0

        mom_id = mom_id_seq; mom_id_seq += 1
        status_id_line = 86 if qty_issued >= qty_required and qty_required > 0 else (145 if qty_issued > 0 else 129)
        MO_MATERIAL.append({
            "mom_id": mom_id,
            "moh_id": moh_id,
            "mo_number": mo_number,
            "bom_ID": 8000 + line_no,
            "Line_Number": line_no,
            "ici_id": mat["ici_id"],
            "item_number": item_number,
            "Item_Number": item_number,
            "item_description": mat["description"],
            "Item_Description": mat["description"],
            "uom": mat["uom"],
            "UOM": mat["uom"],
            "qty_required": qty_required,
            "Qty_Required": qty_required,
            "qty_issued": qty_issued,
            "Qty_Issued": qty_issued,
            "qty_scrap": qty_scrap,
            "Qty_Scrap": qty_scrap,
            "qty_waste": 0,
            "Status_id": status_id_line,
        })
        mol_id = mol_id_seq; mol_id_seq += 1
        MO_LINE.append({
            "mol_ID": mol_id,
            "moh_id": moh_id,
            "moh_ID": moh_id,
            "Mo_Number": mo_number,
            "mo_number": mo_number,
            "Line_No": line_no,
            "Line_Item_Number": item_number,
            "Item_Number": item_number,
            "Line_Item_Description": mat["description"],
            "Location": f"BIN-{random.choice(['A','B','C'])}{random.randint(1,24):02d}",
            "Stores_To_Lab": 0,
            "Is_Parent_Item": 0,
            "MO_Qty_Issued": qty_issued,
            "Qty_Issued": qty_issued,
            "Qty_Required": qty_required,
            "Qty_Complete": 0,
            "Qty_Transferred": 0,
            "Qty_Scrapped": qty_scrap,
            "Datetime_Create": iso(datetime_create),
        })
        total_required += qty_required
        total_issued += qty_issued

    # ---- Header-level derived quantities ---------------------------------------
    qty_complete = 0
    qty_transferred = 0
    qty_scrapped = round(total_issued * random.uniform(0, 0.01), 1)
    completion_date = None

    if stage in ("issued", "partial_transfer", "transferred", "completed"):
        qty_complete = qty if stage in ("transferred", "completed") else round(qty * random.uniform(0.4, 0.95))
    if stage == "partial_transfer":
        qty_transferred = round(qty * random.uniform(0.1, 0.85))
    elif stage in ("transferred", "completed"):
        qty_transferred = qty
    if stage == "completed":
        qty_complete = qty
        completion_date = iso(date_required - timedelta(days=random.randint(0, 6)))

    status_text = {
        "new": "New MO", "started": "Started", "partial_issue": "Started",
        "issued": "Issued", "partial_transfer": "Issued", "transferred": "Transferred",
        "completed": "Completed",
    }[stage]
    status_id = STATUS_TEXT_TO_ID[status_text]

    mo.update({
        "status": status_text,
        "Status": status_text,
        "status_id": status_id,
        "Status_ID": status_id,
        "Qty_Complete": qty_complete,
        "qty_completed": qty_complete,
        "Qty_Issued": round(total_issued, 1),
        "Qty_Transferred": qty_transferred,
        "qty_transferred": qty_transferred,
        "Qty_Scrapped": qty_scrapped,
        "Completion_Date": completion_date,
        "completion_date": completion_date,
    })
    mo["_stage_internal"] = stage  # kept for generator use only; stripped before save

    # ---- Transfer records --------------------------------------------------
    if qty_transferred > 0:
        remaining = qty_transferred
        num_transfers = random.randint(1, 3)
        for t in range(num_transfers):
            chunk = round(remaining / (num_transfers - t)) if t < num_transfers - 1 else remaining
            chunk = max(1, chunk)
            remaining -= chunk
            tdate = date_required - timedelta(days=random.randint(0, 20))
            MO_TRANSFER.append({
                "id": transfer_id_seq,
                "moh_ID": moh_id,
                "mo_number": mo_number,
                "Datetime_Transfer": iso(tdate),
                "Qty_Transfer": chunk,
                "Is_Paired": 1,
            })
            transfer_id_seq += 1

    # ---- Status change history events --------------------------------------
    def add_event(name_status, when, user):
        global event_id_seq
        STATUS_EVENTS.append({
            "id": event_id_seq, "moh_id": moh_id, "mo_number": mo_number,
            "name": user, "event_time": iso(when), "status": name_status,
            "status_id": STATUS_TEXT_TO_ID.get(name_status, 0),
        })
        event_id_seq += 1

    add_event("New MO", datetime_create, "SYSTEM")
    add_event("Released", datetime_create + timedelta(hours=random.randint(1, 20)), "LANGA")
    if stage != "new":
        add_event("Started", datetime_create + timedelta(days=random.randint(1, 4)), random.choice(PRODUCTION_USERS)["employee_username"])
    if stage in ("partial_issue", "issued", "partial_transfer", "transferred", "completed"):
        add_event("Issued", datetime_create + timedelta(days=random.randint(2, 8)), "DANI")
    if stage in ("partial_transfer", "transferred", "completed"):
        add_event("Transferred", datetime_create + timedelta(days=random.randint(6, 15)), "DANI")
    if stage == "completed":
        add_event("Completed", datetime.fromisoformat(completion_date), "SIZWE")

    # ---- Comments (only a handful of MOs) -----------------------------------
    if random.random() < 0.15:
        comment_options = ["TEST MO", "Rush - customer priority", "Awaiting stock on connectors",
                           "Confirm revision with engineering", "Customer requested early delivery",
                           "Hold for QA re-check"]
        MO_COMMENTS.append({
            "id": comment_id_seq, "mo_number": mo_number,
            "comment": random.choice(comment_options),
            "created_by": random.choice(["LANGA", "DANI", "SAM"]),
            "created_at": iso(TODAY - timedelta(days=random.randint(0, 20))),
        })
        comment_id_seq += 1

    # ---- Production workstation cascade (mo_workstation_completions) --------
    if stage in ("started", "partial_issue", "issued", "partial_transfer", "transferred", "completed"):
        # How far through the 9 stages this MO has progressed
        if stage == "completed":
            stages_done = 9
        elif stage in ("transferred", "partial_transfer"):
            stages_done = random.randint(7, 9)
        elif stage == "issued":
            stages_done = random.randint(4, 8)
        else:
            stages_done = random.randint(1, 4)

        input_qty = qty
        assigned_worker = None
        for s_idx in range(stages_done if stage != "completed" or True else 9):
            if s_idx >= 9:
                break
            ws = WORKSTATIONS[s_idx]
            worker = random.choice([w for w in PRODUCTION_USERS if w["workstation_id"] == ws["id"]] or PRODUCTION_USERS)
            is_last_active = (s_idx == stages_done - 1) and stage not in ("completed",)
            qty_rejected = random.choice([0, 0, 0, 1, 2]) if input_qty > 5 else 0
            if is_last_active and stage in ("started", "partial_issue"):
                qty_completed_stage = round(input_qty * random.uniform(0.2, 0.85))
            else:
                qty_completed_stage = max(0, input_qty - qty_rejected)
            output_qty = qty_completed_stage
            balance = input_qty - output_qty
            started_at = datetime_create + timedelta(days=s_idx + 1, hours=random.randint(0, 6))
            is_completed = 1 if (output_qty >= input_qty or stage == "completed") else 0
            completed_at = started_at + timedelta(hours=random.randint(1, 8)) if is_completed else None
            WORKSTATION_COMPLETIONS.append({
                "id": completion_id_seq,
                "mo_number": mo_number,
                "workstation_id": ws["id"],
                "workstation_name": ws["name"],
                "stage_sequence": ws["display_order"],
                "input_qty": input_qty,
                "qty_completed": qty_completed_stage,
                "qty_rejected": qty_rejected,
                "output_qty": output_qty,
                "balance": balance,
                "is_active": 0 if is_completed else 1,
                "is_completed": is_completed,
                "started_at": iso(started_at),
                "completed_at": iso(completed_at) if completed_at else None,
                "created_by": worker["employee_username"],
                "created_at": iso(started_at),
                "last_updated_by": worker["employee_username"],
                "last_updated_at": iso(completed_at) if completed_at else iso(started_at),
            })
            completion_id_seq += 1
            input_qty = output_qty
            assigned_worker = worker

        # ---- Live MO assignment (current workstation) -----------------------------
        if stage not in ("completed",) and stages_done < 9:
            current_ws = WORKSTATIONS[min(stages_done, 8)]
            worker = assigned_worker or random.choice(PRODUCTION_USERS)
            MO_ASSIGNMENTS.append({
                "id": assignment_id_seq,
                "mo_number": mo_number,
                "moh_ID": moh_id,
                "employee_username": worker["employee_username"],
                "user_name": worker["full_name"],
                "workstation": current_ws["name"],
                "workstation_id": current_ws["id"],
                "production_user_id": worker["id"],
                "assigned_by": "LANGA",
                "assigned_at": iso(TODAY - timedelta(days=random.randint(0, 10), hours=random.randint(0, 23))),
                "is_priority": is_priority,
                "notes": None,
                "workstations": None,
            })
            assignment_id_seq += 1

    # ---- Warehouse issue log (Reports) for issued/partial MOs -----------------
    if total_issued > 0:
        for _ in range(random.randint(1, 3)):
            item_number = random.choice(chosen_items)
            REPORTS.append({
                "id": report_id_seq, "action": "issue", "mo": mo_number,
                "item": item_number, "qty": random.randint(1, 40),
                "batch_no": f"B{random.randint(1000,9999)}", "mode": "normal",
                "issued_by": random.choice(["DANI", "LANGA"]),
                "time": iso(datetime_create + timedelta(days=random.randint(1, 10))),
                "notes": None, "items": None,
                "created_at": iso(datetime_create + timedelta(days=random.randint(1, 10))),
            })
            report_id_seq += 1

# Strip internal-only helper key
for mo in MOS:
    mo.pop("_stage_internal", None)

# ---------------------------------------------------------------------------
# 6. BULK WAREHOUSE STOCK (MOTrack.dbo.WHMOItems) - stock control / shortages
# ---------------------------------------------------------------------------
required_by_item = {}
for line in MO_MATERIAL:
    item = line["item_number"]
    outstanding = max(0.0, line["Qty_Required"] - line["Qty_Issued"])
    required_by_item[item] = required_by_item.get(item, 0.0) + outstanding

WHMOITEMS = []
for i, mat in enumerate(MATERIALS):
    item_number = mat["item_number"]
    required_qty = round(required_by_item.get(item_number, 0.0), 1)
    # ~40% of items intentionally understocked to demonstrate shortage reporting
    if random.random() < 0.4:
        total_stock = round(required_qty * random.uniform(0.2, 0.85), 1)
    else:
        total_stock = round(required_qty * random.uniform(1.05, 2.5) + random.uniform(50, 300), 1)
    shortage = max(0.0, round(required_qty - total_stock, 1))
    WHMOITEMS.append({
        "id": i + 1,
        "item_number": item_number,
        "description": mat["description"],
        "ip_address": None,
        "total_stock": total_stock,
        "required_qty": required_qty,
        "required_qty_db": required_qty,
        "last_add": round(random.uniform(20, 200), 1),
        "shortage": shortage,
        "short": shortage,
        "location": f"BIN-{random.choice(['A','B','C','D'])}{random.randint(1,30):02d}",
        "stock_on_hand": total_stock,
        "stock_ordered": round(shortage * random.uniform(0, 1.2), 1) if shortage > 0 else 0.0,
        "on_order": round(shortage * random.uniform(0, 1.2), 1) if shortage > 0 else 0.0,
        "updated_at": iso(TODAY - timedelta(hours=random.randint(1, 96))),
    })

# ---------------------------------------------------------------------------
# 7. REISSUE REQUESTS (MOTrack.dbo.reissue_requests)
# ---------------------------------------------------------------------------
REISSUE_REQUESTS = []
issued_mos = [m for m in MOS if m["Qty_Issued"] and m["Qty_Issued"] > 0]
reasons = [
    "Damaged connectors during installation", "Extra crimp ferrules needed - miscount on first pick",
    "Boots perished in storage, need replacements", "Additional cable required - measurement error",
    "Splice tray cracked in transit", "Short-supplied on last pick, topping up",
]
for i in range(12):
    mo = random.choice(issued_mos)
    mo_lines = [l for l in MO_MATERIAL if l["moh_id"] == mo["moh_id"]]
    items = random.sample(mo_lines, k=min(2, len(mo_lines)))
    status = random.choices(["pending", "accepted", "rejected", "done"], weights=[35, 25, 15, 25], k=1)[0]
    requested_at = TODAY - timedelta(days=random.randint(0, 25), hours=random.randint(0, 23))
    entry = {
        "id": i + 1,
        "mo_number": mo["mo_number"],
        "moh_ID": mo["moh_id"],
        "requested_by": "sizwe@dsawarehouse.demo",
        "requested_by_name": "SIZWE Dube",
        "reason": random.choice(reasons),
        "items": [{"item_number": l["item_number"], "qty_requested": random.randint(2, 15)} for l in items],
        "status": status,
        "requested_at": iso(requested_at),
        "reviewed_by": None,
        "reviewed_by_name": None,
        "reviewed_at": None,
        "admin_response": None,
    }
    if status != "pending":
        entry["reviewed_by"] = "langa@dsawarehouse.demo"
        entry["reviewed_by_name"] = "LANGA Ngidi"
        entry["reviewed_at"] = iso(requested_at + timedelta(hours=random.randint(1, 30)))
        entry["admin_response"] = {
            "accepted": "Approved - will reissue today", "rejected": "Denied - recount stock first",
            "done": "Reissue completed",
        }[status]
    REISSUE_REQUESTS.append(entry)

# ---------------------------------------------------------------------------
# Assemble & save
# ---------------------------------------------------------------------------
DATA = {
    "meta": {"generated_at": iso(TODAY), "today_anchor": iso(TODAY)},
    "users": USERS,
    "workstations": WORKSTATIONS,
    "production_users": PRODUCTION_USERS,
    "materials": MATERIALS,
    "customers": [{"code": c, "name": n} for c, n in CUSTOMERS],
    "mos": MOS,
    "mo_material": MO_MATERIAL,
    "mo_line": MO_LINE,
    "mo_transfer": MO_TRANSFER,
    "status_events": STATUS_EVENTS,
    "mo_assignments": MO_ASSIGNMENTS,
    "mo_comments": MO_COMMENTS,
    "workstation_completions": WORKSTATION_COMPLETIONS,
    "reports": REPORTS,
    "whmoitems": WHMOITEMS,
    "reissue_requests": REISSUE_REQUESTS,
    "action_logs": [],
    "next_ids": {
        "mom_id": mom_id_seq, "mol_id": mol_id_seq, "transfer_id": transfer_id_seq,
        "event_id": event_id_seq, "assignment_id": assignment_id_seq, "comment_id": comment_id_seq,
        "completion_id": completion_id_seq, "report_id": report_id_seq,
        "reissue_id": len(REISSUE_REQUESTS) + 1, "whmoitem_id": len(WHMOITEMS) + 1,
    },
}

with open(OUT_SEED, "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2)

print(f"Generated {len(MOS)} MOs, {len(MO_MATERIAL)} BOM lines, {len(WHMOITEMS)} bulk stock items, "
      f"{len(REISSUE_REQUESTS)} reissue requests, {len(WORKSTATION_COMPLETIONS)} workstation completion rows.")
print(f"Wrote {OUT_SEED}")
