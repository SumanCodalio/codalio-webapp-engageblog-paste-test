import json
from datetime import datetime, timezone

with open('.codalio/acceptance-criteria.json', 'r') as f:
    data = json.load(f)

test_map = {
    'AC-1': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-2': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-3': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-4': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-5': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-6': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-7': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-8': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-9': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-10': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-11': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',
    'AC-12': 'test/integration/acceptance_criteria_test.rb#test_AC-1_to_AC-12:_Create,_view,_edit_and_publish_posts',

    'AC-13': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',
    'AC-14': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',
    'AC-15': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',
    'AC-16': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',
    'AC-17': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',
    'AC-18': 'test/integration/acceptance_criteria_test.rb#test_AC-13_to_AC-18:_Upload_and_store_videos',

    'AC-19': 'test/integration/acceptance_criteria_test.rb#test_AC-19_to_AC-22:_Embed_video_in_post',
    'AC-20': 'test/integration/acceptance_criteria_test.rb#test_AC-19_to_AC-22:_Embed_video_in_post',
    'AC-21': 'test/integration/acceptance_criteria_test.rb#test_AC-19_to_AC-22:_Embed_video_in_post',
    'AC-22': 'test/integration/acceptance_criteria_test.rb#test_AC-19_to_AC-22:_Embed_video_in_post',

    'AC-23': 'test/integration/acceptance_criteria_test.rb#test_AC-23_to_AC-26:_Authentication_and_Login',
    'AC-24': 'test/integration/acceptance_criteria_test.rb#test_AC-23_to_AC-26:_Authentication_and_Login',
    'AC-25': 'test/integration/acceptance_criteria_test.rb#test_AC-23_to_AC-26:_Authentication_and_Login',
    'AC-26': 'test/integration/acceptance_criteria_test.rb#test_AC-23_to_AC-26:_Authentication_and_Login',

    'AC-27': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-28': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-29': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-30': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-31': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-32': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-33': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',

    'AC-34': 'test/integration/acceptance_criteria_test.rb#test_AC-34_to_AC-36:_Logout_functionality',
    'AC-35': 'test/integration/acceptance_criteria_test.rb#test_AC-34_to_AC-36:_Logout_functionality',
    'AC-36': 'test/integration/acceptance_criteria_test.rb#test_AC-34_to_AC-36:_Logout_functionality',

    'AC-37': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-38': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-39': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-40': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-41': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-42': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-43': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-44': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',
    'AC-45': 'test/integration/acceptance_criteria_test.rb#test_AC-37_to_AC-45:_Analytics_access_and_filtering',

    'AC-56': 'test/integration/acceptance_criteria_test.rb#test_AC-56_to_AC-58:_RBAC',
    'AC-57': 'test/integration/acceptance_criteria_test.rb#test_AC-56_to_AC-58:_RBAC',
    'AC-58': 'test/integration/acceptance_criteria_test.rb#test_AC-56_to_AC-58:_RBAC',

    'AC-59': 'test/integration/acceptance_criteria_test.rb#test_AC-59:_Dashboard_stats_endpoint',
    'AC-60': 'test/integration/acceptance_criteria_test.rb#test_AC-27_to_AC-33,_AC-60:_Manage_users',
    'AC-61': 'test/integration/acceptance_criteria_test.rb#test_AC-61:_Data_Seeding_provides_roles_and_sample_users'
}

for c in data['criteria']:
    if c['id'] in test_map:
        c['status'] = 'tested'
        c['test_name'] = test_map[c['id']]

data['updated_at'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

with open('.codalio/acceptance-criteria.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated criteria!")
