def merge_data(inspection_data, thermal_data):
    merged = {}

    all_areas = set(inspection_data.keys()) | set(thermal_data.keys())

    for area in all_areas:
        merged[area] = {
            "observation": inspection_data.get(area, "Not Available"),
            "thermal": thermal_data.get(area, "Not Available")
        }

    return merged