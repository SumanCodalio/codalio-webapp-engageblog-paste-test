import json
from datetime import datetime, timezone

def update_ac():
    with open("../.codalio/acceptance-criteria.json", "r") as f:
        data = json.load(f)

    test_file = "test/integration/acceptance_criteria_test.rb"

    passed_acs = [
        "AC-1", "AC-2", "AC-3", "AC-4", "AC-5", "AC-6", "AC-7", "AC-8", "AC-9", "AC-10", "AC-11", "AC-12",
        "AC-13", "AC-14", "AC-15", "AC-16", "AC-17", "AC-18",
        "AC-19", "AC-20", "AC-21", "AC-22",
        "AC-23", "AC-24", "AC-25", "AC-26",
        "AC-27", "AC-28", "AC-29", "AC-30", "AC-31", "AC-32", "AC-33",
        "AC-34", "AC-35", "AC-36",
        "AC-37", "AC-38", "AC-39", "AC-40", "AC-41", "AC-42", "AC-43", "AC-44", "AC-45",
        "AC-56", "AC-57", "AC-58",
        "AC-59", "AC-60", "AC-61"
    ]

    mappings = {
        "AC-1": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-2": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-3": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-4": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-5": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-6": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-7": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-8": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-9": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-10": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-11": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",
        "AC-12": "test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts",

        "AC-13": "test_AC-13_to_AC-18:_Upload_and_store_videos",
        "AC-14": "test_AC-13_to_AC-18:_Upload_and_store_videos",
        "AC-15": "test_AC-13_to_AC-18:_Upload_and_store_videos",
        "AC-16": "test_AC-13_to_AC-18:_Upload_and_store_videos",
        "AC-17": "test_AC-13_to_AC-18:_Upload_and_store_videos",
        "AC-18": "test_AC-13_to_AC-18:_Upload_and_store_videos",

        "AC-19": "test_AC-19_to_AC-22:_Embed_video_in_post",
        "AC-20": "test_AC-19_to_AC-22:_Embed_video_in_post",
        "AC-21": "test_AC-19_to_AC-22:_Embed_video_in_post",
        "AC-22": "test_AC-19_to_AC-22:_Embed_video_in_post",

        "AC-23": "test_AC-23_to_AC-26:_Authentication_and_Login",
        "AC-24": "test_AC-23_to_AC-26:_Authentication_and_Login",
        "AC-25": "test_AC-23_to_AC-26:_Authentication_and_Login",
        "AC-26": "test_AC-23_to_AC-26:_Authentication_and_Login",

        "AC-27": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-28": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-29": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-30": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-31": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-32": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-33": "test_AC-27_to_AC-33,_AC-60:_Manage_users",
        "AC-60": "test_AC-27_to_AC-33,_AC-60:_Manage_users",

        "AC-34": "test_AC-34_to_AC-36:_Logout_functionality",
        "AC-35": "test_AC-34_to_AC-36:_Logout_functionality",
        "AC-36": "test_AC-34_to_AC-36:_Logout_functionality",

        "AC-37": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-38": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-39": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-40": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-41": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-42": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-43": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-44": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",
        "AC-45": "test_AC-37_to_AC-45:_Analytics_access_and_filtering",

        "AC-56": "test_AC-56_to_AC-58:_RBAC",
        "AC-57": "test_AC-56_to_AC-58:_RBAC",
        "AC-58": "test_AC-56_to_AC-58:_RBAC",

        "AC-59": "test_AC-59:_Dashboard_stats_endpoint",
        "AC-61": "test_AC-61:_Data_Seeding_provides_roles_and_sample_users"
    }

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    for ac in data["criteria"]:
        ac_id = ac["id"]
        if ac_id in passed_acs:
            ac["status"] = "tested"
            ac["test_name"] = test_file + "#" + mappings[ac_id]

    data["updated_at"] = now

    with open("../.codalio/acceptance-criteria.json", "w") as f:
        json.dump(data, f, indent=2)

update_ac()