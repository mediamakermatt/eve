command_center = {"cpu": 25415, "power": 19000}
# all weight is measured in m3
# delivers to the customs office orbiting the planet, auto-routing of items allowed
launchpad = {"cpu": 3600, "power": 700, "capacity": 10000}
# holds more than launchpad and is cheaper but requires manual routing of items
storage = {"cpu": 500, "power": 700, "capacity": 12000}
# attaches to any other module to deliver the T0 resources mined
extractor_control_unit = {"cpu": 400, "power": 2600}
# 10 nodes can go on each extractor
  # usually 10 full nodes can extract ~2M raw daily
extractor_control_unit_node = {"cpu": 110, "power": 550}

planet_resources = {
    "J121749 I": {
        "radius": 5380,
        "resources": [
        ("Aqueous Liquids", .40), 
        ("Base Metals", .68), 
        ("Carbon Compounds", .75), 
        ("Microorganisms", .68), 
        ("Noble Metals", .48)
        ]
    },
    "J121749 II": {
        "radius": 5500,
        "resources": [
        ("Base Metals", .40), 
        ("Felsic Magma", .42), 
        ("Heavy Metals", .83), 
        ("Non-CS Crystals", .68), 
        ("Suspended Plasma", .51)
        ]
    },
    "J121749 III": {
        "radius": 8100,
        "resources": [
        ("Aqueous Liquids", .39), 
        ("Base Metals", .70), 
        ("Carbon Compounds", .75), 
        ("Microorganisms", .64), 
        ("Noble Metals", .50)
        ]
    },
    "J121749 IV": {
        "radius": 8300,
        "resources": [
        ("Base Metals", .39), 
        ("Felsic Magma", .26), 
        ("Heavy Metals", .75), 
        ("Non-CS Crystals", .70), 
        ("Suspended Plasma", .52)
        ]
    },
    "J121749 V": {
        "radius": 6740,
        "resources": [
        ("Aqueous Liquids", .41), 
        ("Base Metals", .63), 
        ("Carbon Compounds", .70), 
        ("Microorganisms", .68), 
        ("Noble Metals", .41)
        ]
    },
    "J121749 VI": {
        "radius": 11840,
        "resources": [
        ("Aqueous Liquids", .82), 
        ("Base Metals", .74), 
        ("Ionic Solutions", .48), 
        ("Noble Gas", .60), 
        ("Suspended Plasma", .66)
        ]
    },
    "J121749 VII": {
        "radius": 4780,
        "resources": [
        ("Aqueous Liquids", .39), 
        ("Base Metals", .62), 
        ("Carbon Compounds", .69), 
        ("Microorganisms", .71), 
        ("Noble Metals", .43)
        ]
    },
    "J121749 VIII": {
        "radius": 15260,
        "resources": [
        ("Aqueous Liquids", .49), 
        ("Base Metals", .49), 
        ("Ionic Solutions", .59), 
        ("Noble Gas", .78), 
        ("Suspended Plasma", .37)
        ]
    },
    "J121749 IX": {
        "radius": 5780,
        "resources": [
        ("Aqueous Liquids", .41), 
        ("Base Metals", .61), 
        ("Carbon Compounds", .65), 
        ("Microorganisms", .68), 
        ("Noble Metals", .36)
        ]
    }
}

factories = {
    "Raw Materials": [ # Materials mined from the planets
        {"name": "Aqueous Liquids", "volume": 0.005}, 
        {"name": "Autotrophs", "volume": 0.005}, 
        {"name": "Base Metals", "volume": 0.005},
        {"name": "Carbon Compounds", "volume": 0.005}, 
        {"name": "Complex Organisms", "volume": 0.005}, 
        {"name": "Felsic Magma", "volume": 0.005},
        {"name": "Heavy Metals", "volume": 0.005}, 
        {"name": "Ionic Solutions", "volume": 0.005}, 
        {"name": "Microorganisms", "volume": 0.005},
        {"name": "Noble Gas", "volume": 0.005}, 
        {"name": "Noble Metals", "volume": 0.005}, 
        {"name": "Non-CS Crystals", "volume": 0.005},
        {"name": "Planktic Colonies", "volume": 0.005}, 
        {"name": "Reactive Gas", "volume": 0.005}, 
        {"name": "Suspended Plasma", "volume": 0.005}
    ],
    "Basic Industry Facility": [ # Cycle Time is in Minutes
        {"category": "Processed"},
        {"power_load": 800}, {"cpu_load": 200}, {"cycle_time": 30},
        {"name": "Bacteria",
        "inputs": [("Microorganisms", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Biofuels",
        "inputs": [("Carbon Compounds", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Biomass",
        "inputs": [("Planktic Colonies", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Chiral Structures",
        "inputs": [("Non-CS Crystals", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Electrolytes",
        "inputs": [("Ionic Solutions", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Industrial Fibers",
        "inputs": [("Autotrophs", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Oxidizing Compound",
        "inputs": [("Reactive Gas", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Oxygen",
        "inputs": [("Noble Gas", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Plasmoids",
        "inputs": [("Suspended Plasma", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Precious Metals",
        "inputs": [("Noble Metals", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Proteins",
        "inputs": [("Complex Organisms", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Reactive Metals",
        "inputs": [("Base Metals", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Silicon",
        "inputs": [("Felsic Magma", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Toxic Metals",
        "inputs": [("Heavy Metals", 3000)],
        "output_amt": 20, "volume": 7.6},
        {"name": "Water",
        "inputs": [("Aqueous Liquids", 3000)],
        "output_amt": 20, "volume": 7.6}
    ],
    "Advanced Industry Facility": [ # Cycle Time is in Minutes
        {"power_load": 700}, {"cpu_load": 500}, {"cycle_time": 60},
        # Refined
        {"category": "Refined"}, 
        {"name": "Biocells",
            "inputs": [("Biofuels", 40), ("Precious Metals", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Construction Blocks",
            "inputs": [("Toxic Metals", 40), ("Reactive Metals", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Consumer Electronics",
            "inputs": [("Toxic Metals", 40), ("Chiral Structures", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Coolant",
            "inputs": [("Electrolytes", 40), ("Water", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Enriched Uranium",
            "inputs": [("Toxic Metals", 40), ("Precious Metals", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Fertilizer",
            "inputs": [("Bacteria", 40), ("Proteins", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Genetically Enhanced Livestock",
            "inputs": [("Proteins", 40), ("Biomass", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Livestock",
            "inputs": [("Biofuels", 40), ("Proteins", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Mechanical Parts",
            "inputs": [("Reactive Metals", 40), ("Precious Metals", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Microfiber Shielding",
            "inputs": [("Silicon", 40), ("Industrial Fibers", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Miniature Electronics",
            "inputs": [("Silicon", 40), ("Chiral Structures", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Nanites",
            "inputs": [("Reactive Metals", 40), ("Bacteria", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Oxides",
            "inputs": [("Oxidizing Compound", 40), ("Oxygen", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Polyaramids",
            "inputs": [("Oxidizing Compound", 40), ("Industrial Fibers", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Polytextiles",
            "inputs": [("Biofuels", 40), ("Industrial Fibers", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Rocket Fuel",
            "inputs": [("Electrolytes", 40), ("Plasmoids", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Silicate Glass",
            "inputs": [("Oxidizing Compound", 40), ("Silicon", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Superconductors",
            "inputs": [("Plasmoids", 40), ("Water", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Supertensile Plastics",
            "inputs": [("Oxygen", 40), ("Biomass", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Synthetic Oil",
            "inputs": [("Electrolytes", 40), ("Oxygen", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Test Cultures",
            "inputs": [("Bacteria", 40), ("Water", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Transmitter",
            "inputs": [("Chiral Structures", 40), ("Plasmoids", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Viral Agent",
            "inputs": [("Bacteria", 40), ("Biomass", 40)],
            "output_amt": 5, "volume": 3.8},
        {"name": "Water-Cooled CPU",
            "inputs": [("Reactive Metals", 40), ("Water", 40)],
            "output_amt": 5, "volume": 3.8},
        # Specialized
        {"category": "Specialized"},
        {"name": "Biotech Research Reports",
            "inputs": [("Construction Blocks", 10), ("Livestock", 10), ("Nanites", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Camera Drones",
            "inputs": [("Rocket Fuel", 10), ("Silicate Glass", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Condensates",
            "inputs": [("Coolant", 10), ("Oxides", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Cryoprotectant Solution",
            "inputs": [("Synthetic Oil", 10), ("Fertilizer", 10), ("Test Cultures", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Data Chips",
            "inputs": [("Supertensile Plastics", 10), ("Microfiber Shielding", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Gel-Matrix Biopaste",
            "inputs": [("Superconductors", 10), ("Biocells", 10), ("Oxides", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Guidance Systems",
            "inputs": [("Water-Cooled CPU", 10), ("Transmitter", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Hazmat Detection Systems",
            "inputs": [("Transmitter", 10), ("Viral Agent", 10), ("Polytextiles", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Hermetic Membranes",
            "inputs": [("Polyaramids", 10), ("Genetically Enhanced Livestock", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "High-Tech Transmitters",
            "inputs": [("Transmitter", 10), ("Polyaramids", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Industrial Explosives",
            "inputs": [("Fertilizer", 10), ("Polytextiles", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Neocoms",
            "inputs": [("Biocells", 10), ("Silicate Glass", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Nuclear Reactors",
            "inputs": [("Enriched Uranium", 10), ("Microfiber Shielding", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Planetary Vehicles",
            "inputs": [("Supertensile Plastics", 10), ("Miniature Electronics", 10), ("Mechanical Parts", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Robotics",
            "inputs": [("Consumer Electronics", 10), ("Mechanical Parts", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Smartfab Units",
            "inputs": [("Miniature Electronics", 10), ("Construction Blocks", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Supercomputers",
            "inputs": [("Water-Cooled CPU", 10), ("Coolant", 10), ("Consumer Electronics", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Synthetic Synapses",
            "inputs": [("Supertensile Plastics", 10), ("Test Cultures", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Transcranial Microcontrollers",
            "inputs": [("Biocells", 10), ("Nanites", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Ukomi Superconductors",
            "inputs": [("Superconductors", 10), ("Synthetic Oil", 10)],
            "output_amt": 3, "volume": 9},
        {"name": "Vaccines",
            "inputs": [("Livestock", 10), ("Viral Agent", 10)],
            "output_amt": 3, "volume": 9}
    ],
    "High Tech Production Plant": [ # Cycle Time is in Minutes
        {"power_load": 400}, {"cpu_load": 1100}, {"cycle_time": 60},
        {"category": "Advanced"}, 
        {"name": "Broadcast Node", 
        "inputs": [("Data Chips", 6), ("Neocoms", 6), ("High-Tech Transmitters", 6)],
        "output_amt": 1, "volume": 50},
        {"name": "Integrity Response Drones", 
        "inputs": [("Gel-Matrix Biopaste", 6), ("Planetary Vehicles", 6), ("Hazmat Detection Systems", 6)],
        "output_amt": 1, "volume": 50},
        {"name": "Nano-Factory", 
        "inputs": [("Industrial Explosives", 6), ("Ukomi Superconductors", 6), ("Reactive Metals", 40)],
        "output_amt": 1, "volume": 50},
        {"name": "Organic Mortar Applicators", 
        "inputs": [("Condensates", 6), ("Robotics", 6), ("Bacteria", 40)],
        "output_amt": 1, "volume": 50},
        {"name": "Recursive Computing Module", 
        "inputs": [("Synthetic Synapses", 6), ("Transcranial Microcontrollers", 6), ("Guidance Systems", 6)],
        "output_amt": 1, "volume": 50},
        {"name": "Self-Harmonizing Power Core",
        "inputs": [("Nuclear Reactors", 6), ("Camera Drones", 6), ("Hermetic Membranes", 6)],
        "output_amt": 1, "volume": 50},
        {"name": "Sterile Conduits",
        "inputs": [("Vaccines", 6), ("Water", 40), ("Smartfab Units", 6)],
        "output_amt": 1, "volume": 50},
        {"name": "Wetware Mainframe", 
        "inputs": [("Biotech Research Reports", 6), ("Supercomputers", 6), ("Cryoprotectant Solution", 6)],
        "output_amt": 1, "volume": 50}
    ],
}

def find_top_factories_per_planet(planet_resources, factories, top_n=3):
    from collections import defaultdict

    raw_names = {item["name"] for item in factories["Raw Materials"]}
    basic_recipes = [item for item in factories["Basic Industry Facility"] if isinstance(item, dict) and "name" in item]
    advanced_recipes = [item for item in factories["Advanced Industry Facility"] if isinstance(item, dict) and "name" in item]
    high_tech_recipes = [item for item in factories["High Tech Production Plant"] if isinstance(item, dict) and "name" in item]

    all_recipes = {
        "Basic": basic_recipes,
        "Advanced": advanced_recipes,
        "HighTech": high_tech_recipes
    }

    tier_weights = {"Basic": 1, "Advanced": 2, "HighTech": 3}
    volume_weight = 0.1
    input_weight = 0.05

    output_to_recipe = {}
    for tier, recipes in all_recipes.items():
        for r in recipes:
            output_to_recipe[r["name"]] = (r, tier)

    def is_buildable(product_name, available, tier):
        recipe_data = output_to_recipe.get(product_name)
        if not recipe_data:
            return False
        recipe, _ = recipe_data
        for input_name, _ in recipe["inputs"]:
            if input_name not in available:
                if tier == "Basic":
                    return False
                if not is_buildable(input_name, available, "Basic"):
                    return False
        return True

    best_factories = {}

    for planet, pdata in planet_resources.items():
        raw = {res[0] for res in pdata["resources"]}
        buildable = set(raw)
        buildable_recipes = []

        # Basic
        for r in basic_recipes:
            if all(ri[0] in raw for ri in r["inputs"]):
                buildable.add(r["name"])
                score = (tier_weights["Basic"] +
                         r["volume"] * volume_weight +
                         len(r["inputs"]) * input_weight)
                buildable_recipes.append((r["name"], "Basic", score))

        # Advanced
        for r in advanced_recipes:
            if is_buildable(r["name"], buildable, "Advanced"):
                buildable.add(r["name"])
                score = (tier_weights["Advanced"] +
                         r["volume"] * volume_weight +
                         len(r["inputs"]) * input_weight)
                buildable_recipes.append((r["name"], "Advanced", score))

        # High Tech
        for r in high_tech_recipes:
            if is_buildable(r["name"], buildable, "HighTech"):
                buildable.add(r["name"])
                score = (tier_weights["HighTech"] +
                         r["volume"] * volume_weight +
                         len(r["inputs"]) * input_weight)
                buildable_recipes.append((r["name"], "HighTech", score))

        # Sort by score descending
        buildable_recipes.sort(key=lambda x: -x[2])
        best_factories[planet] = buildable_recipes[:top_n]

    return best_factories

results = find_top_factories_per_planet(planet_resources, factories)

for planet, recipes in results.items():
    print(f"\n{planet}:")
    for name, tier, score in recipes:
        print(f" - {name} (Tier: {tier}, Score: {score:.2f})")

def get_factory_stats(factory_list):
    cpu = next((entry.get("cpu_load") for entry in factory_list if isinstance(entry, dict) and "cpu_load" in entry), None)
    power = next((entry.get("power_load") for entry in factory_list if isinstance(entry, dict) and "power_load" in entry), None)
    return cpu, power

def estimate_factory_capacity(cpu_budget=24144, power_budget=18050, reserve_cpu=6700, reserve_power=9800):
    available_cpu = cpu_budget - reserve_cpu
    available_power = power_budget - reserve_power

    factory_limits = {}

    def max_units(cpu_cost, power_cost):
        return min(available_cpu // cpu_cost, available_power // power_cost)

    basic_cpu, basic_power = get_factory_stats(factories["Basic Industry Facility"])
    adv_cpu, adv_power = get_factory_stats(factories["Advanced Industry Facility"])
    ht_cpu, ht_power = get_factory_stats(factories["High Tech Production Plant"])

    factory_limits['Basic'] = max_units(basic_cpu, basic_power)
    factory_limits['Advanced'] = max_units(adv_cpu, adv_power)
    factory_limits['HighTech'] = max_units(ht_cpu, ht_power)



    return {
        'Available CPU': available_cpu,
        'Available Power': available_power,
        'Max Factories': factory_limits
    }

print(f" ")

# Example usage
limits = estimate_factory_capacity()
for k, v in limits.items():
    print(f"{k}: {v}")

print(f" ")

def estimate_planetary_setup_for_recipe(recipe_name, planet_raws, factories, command_center, buffer_pct=0.00):
    import math

    # Helper to get static CPU/Power for factories
    def get_factory_stats(factory_list):
        cpu = next((entry["cpu_load"] for entry in factory_list if isinstance(entry, dict) and "cpu_load" in entry), None)
        power = next((entry["power_load"] for entry in factory_list if isinstance(entry, dict) and "power_load" in entry), None)
        return cpu, power


    # Gather relevant factory info
    basic_recipes = [f for f in factories["Basic Industry Facility"] if isinstance(f, dict) and "name" in f]
    advanced_recipes = [f for f in factories["Advanced Industry Facility"] if isinstance(f, dict) and "name" in f]
    basic_map = {r["name"]: r for r in basic_recipes}

    basic_cpu, basic_power = get_factory_stats(factories["Basic Industry Facility"])
    adv_cpu, adv_power = get_factory_stats(factories["Advanced Industry Facility"])

    # Static structure specs (per in-game)
    extractor_cpu = extractor_control_unit["cpu"]
    extractor_power = extractor_control_unit["power"]

    node_cpu = extractor_control_unit_node["cpu"]
    node_power = extractor_control_unit_node["power"]

    launchpad_cpu = launchpad["cpu"]
    launchpad_power = launchpad["power"]
    launchpad_capacity = launchpad["capacity"]

    storage_cpu = storage["cpu"]
    storage_power = storage["power"]
    storage_capacity = storage["capacity"]


    # Command Center limits w/ buffer
    max_cpu = command_center["cpu"] * (1 - buffer_pct)
    max_power = command_center["power"] * (1 - buffer_pct)

    # Get the recipe object
    recipe = next((r for r in advanced_recipes if r["name"] == recipe_name), None)
    if not recipe:
        return None

    adv_factory_count = 1
    best_setup = None

    while True:
        # Step 1: Compute daily input needs for advanced factories
        adv_cycles_per_day = 24
        input_needs = [(inp[0], inp[1] * adv_factory_count * adv_cycles_per_day) for inp in recipe["inputs"]]

        total_basic = 0
        t0_needs = {}
        basic_outputs = {}
        valid = True

        for name, qty in input_needs:
            basic = basic_map.get(name)
            if not basic:
                valid = False
                break

            basic_output_per_day = 20 * 48  # per factory
            num_basic = math.ceil(qty / basic_output_per_day)
            total_basic += num_basic
            basic_outputs[name] = num_basic

            for raw, _ in basic["inputs"]:
                if raw not in planet_raws:
                    valid = False
                    break
                t0_needs[raw] = t0_needs.get(raw, 0) + 144000 * num_basic  # per day

        if not valid:
            break

        # Step 2: Assign nodes and ECUs per resource
        nodes_per_resource = {}
        total_nodes = 0
        ecus = 0
        for raw, amount in t0_needs.items():
            nodes = math.ceil(amount / 200000)  # 200k/day/node
            nodes_per_resource[raw] = nodes
            total_nodes += nodes
            ecus += math.ceil(nodes / 10)  # 10 nodes per ECU

        # Step 3: Launchpad is always present
        launchpads = 1

        # Step 4: Calculate volume output to determine storage needs
        basic_output_volume = total_basic * 20 * 48 * 7.6
        adv_output_volume = adv_factory_count * 5 * 24 * 3.8
        total_volume = basic_output_volume + adv_output_volume

        storage_volume_needed = total_volume - (launchpad_capacity * launchpads)
        storages = math.ceil(storage_volume_needed / storage_capacity) if storage_volume_needed > 0 else 0

        # Step 5: Compute total CPU and Power usage
        total_cpu = (
            basic_cpu * total_basic +
            adv_cpu * adv_factory_count +
            extractor_cpu * ecus +
            node_cpu * total_nodes +
            launchpad_cpu * launchpads +
            storage_cpu * storages
        )
        total_power = (
            basic_power * total_basic +
            adv_power * adv_factory_count +
            extractor_power * ecus +
            node_power * total_nodes +
            launchpad_power * launchpads +
            storage_power * storages
        )

        # Step 6: If too expensive, stop and return best from previous loop
        if total_cpu > max_cpu or total_power > max_power:
            break

        best_setup = {
            "recipe": recipe_name,
            "advanced_factories": adv_factory_count,
            "basic_factories": total_basic,
            "extractors": ecus,
            "nodes": total_nodes,
            "launchpads": launchpads,
            "storages": storages,
            "cpu_used": total_cpu,
            "power_used": total_power,
            "cpu_max": max_cpu,
            "power_max": max_power,
            "t0_required": t0_needs,
            "node_distribution": nodes_per_resource,
            "daily_output_volume": total_volume
        }

        adv_factory_count += 1

    return best_setup



def analyze_all_planets(planet_resources, factories, command_center):
    from collections import defaultdict

    # Helper for retrieving only recipe data
    advanced_recipes = [r for r in factories["Advanced Industry Facility"] if isinstance(r, dict) and "name" in r]

    tier_weights = {"Basic": 1, "Advanced": 2, "HighTech": 3}
    volume_weight = 0.1
    input_weight = 0.05

    output_to_recipe = {r["name"]: r for r in advanced_recipes}

    def recipe_score(r):
        return (tier_weights["Advanced"] +
                r["volume"] * volume_weight +
                len(r["inputs"]) * input_weight)

    results = {}

    for planet, pdata in planet_resources.items():
        raw_set = {r[0] for r in pdata["resources"]}
        viable = []

        for recipe in advanced_recipes:
            inputs = [i[0] for i in recipe["inputs"]]
            # Check if all required T0 inputs exist locally through basic processing
            basic_ok = True
            for name in inputs:
                # Find the basic recipe that makes it
                found = False
                for b in factories["Basic Industry Facility"]:
                    if isinstance(b, dict) and b.get("name") == name:
                        # Check if its T0 input exists on the planet
                        for t0, _ in b["inputs"]:
                            if t0 not in raw_set:
                                basic_ok = False
                                break
                        found = True
                        break
                if not found or not basic_ok:
                    basic_ok = False
                    break
            if basic_ok:
                viable.append(recipe)

        # Rank viable recipes by score
        viable.sort(key=recipe_score, reverse=True)

        for recipe in viable:
            setup = estimate_planetary_setup_for_recipe(recipe["name"], raw_set, factories, command_center)
            if setup:
                results[planet] = setup
                break
        else:
            results[planet] = {"recipe": None}

    # Final reporting
    for planet, result in results.items():
        print(f"\n🪐 {planet}")
        if not result.get("recipe"):
            print(" - ❌ No viable setup fits within CPU/Power constraints.")
            continue
        print(f" - ✅ Best Recipe: {result['recipe']}")
        print(f"   • Advanced Factories: {result['advanced_factories']}")
        print(f"   • Basic Factories: {result['basic_factories']}")
        print(f"   • Extractor Units: {result['extractors']}")
        print(f"   • Nodes: {result['nodes']}")
        print(f"   • CPU Used: {result['cpu_used']:.0f} / {result['cpu_max']:.0f}")
        print(f"   • Power Used: {result['power_used']:.0f} / {result['power_max']:.0f}")
        cpu_pct = setup["cpu_used"] / setup["cpu_max"] * 100
        power_pct = setup["power_used"] / setup["power_max"] * 100
        print(f"   • CPU Usage: {cpu_pct:.1f}%")
        print(f"   • Power Usage: {power_pct:.1f}%")
        print(f"   • Launchpads: {result['launchpads']}")
        print(f"   • Storage Units: {result['storages']}")
        print(f"   • Total Output Volume: {result['daily_output_volume']:.0f} m³ / day")
        print(f"   • T0 Required: {result['t0_required']}")


analyze_all_planets(planet_resources, factories, command_center)
