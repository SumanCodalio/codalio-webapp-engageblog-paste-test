import json
import datetime

criteria = [
    ("AC-1", "Only content_team_member can access /create-post.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-2", "User can enter and format text content using a rich text editor.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-3", "User can save a post as a draft.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-4", "User can preview the post before publishing.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-5", "User can publish the post, making it live.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-6", "Published posts are visible on the blog.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/dashboard/LandingPage.tsx"]),
    ("AC-7", "The data model stores approved and the application uses it as described in this story.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["bundle exec rails g migration AddFieldsToUsers approved:boolean profile_completed:boolean first_name:string last_name:string"]),
    ("AC-8", "The data model stores profile completed and the application uses it as described in this story.", "Create and Publish Text Post", "Phase 1: Minimum Viable Product (MVP)", ["db/migrate/*_add_fields_to_users.rb"]),
    ("AC-9", "Only content_team_member can edit published posts.", "Edit Existing Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-10", "User can select a published post from a list and enter edit mode.", "Edit Existing Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/dashboard/LandingPage.tsx"]),
    ("AC-11", "User can modify text and media within the post.", "Edit Existing Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-12", "User can save changes, which are immediately reflected on the live blog.", "Edit Existing Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-13", "Only content_team_member can access /media-library.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/media/MediaLibraryPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-14", "The app provides an upload UI for video data, accepting MP4, MOV, and AVI formats, and visibly confirms a successful import.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/media/MediaLibraryPage.tsx"]),
    ("AC-15", "User can add a title and description to the uploaded video.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/media/MediaLibraryPage.tsx"]),
    ("AC-16", "Uploaded videos are stored in the media library.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/media/MediaLibraryPage.tsx"]),
    ("AC-17", "The data model stores duration and the application uses it as described in this story.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["bundle exec rails rhino:blueprint"]),
    ("AC-18", "The data model stores url and the application uses it as described in this story.", "Upload Video Content", "Phase 1: Minimum Viable Product (MVP)", ["bundle exec rails rhino:blueprint"]),
    ("AC-19", "Only content_team_member can embed videos.", "Embed Video in Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-20", "User can select an uploaded video from the media library within the post editor.", "Embed Video in Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-21", "The selected video is correctly embedded and displayed in the post preview.", "Embed Video in Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-22", "Embedded videos play correctly on the published blog post.", "Embed Video in Post", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/posts/CreatePostPage.tsx"]),
    ("AC-23", "Unauthenticated users are redirected to /login when accessing /admin/dashboard.", "Admin Login", "Phase 1: Minimum Viable Product (MVP)", ["client/src/routes/custom.jsx"]),
    ("AC-24", "User can enter email and password on the login page.", "Admin Login", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/auth/LoginPage.tsx"]),
    ("AC-25", "Successful login redirects admin to /admin/dashboard.", "Admin Login", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/auth/LoginPage.tsx"]),
    ("AC-26", "Failed login attempts display an error message.", "Admin Login", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/auth/LoginPage.tsx"]),
    ("AC-27", "Only admin can access /admin/users.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/admin/AdminUsersPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-28", "Admin can view a list of existing content_team_member accounts.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/admin/AdminUsersPage.tsx"]),
    ("AC-29", "Admin can create a new content_team_member account with a name, email, and password.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/admin/AdminUsersPage.tsx"]),
    ("AC-30", "Admin can edit an existing content_team_member's details.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/admin/AdminUsersPage.tsx"]),
    ("AC-31", "Admin can deactivate or delete a content_team_member account.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/admin/AdminUsersPage.tsx"]),
    ("AC-32", "The data model stores first name and the application uses it as described in this story.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["db/migrate/*_add_fields_to_users.rb"]),
    ("AC-33", "The data model stores last name and the application uses it as described in this story.", "Manage Content Team Members", "Phase 1: Minimum Viable Product (MVP)", ["db/migrate/*_add_fields_to_users.rb"]),
    ("AC-34", "User can click a logout button.", "User Logout", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/layout/AppLayout.tsx"]),
    ("AC-35", "Successful logout redirects the user to /login.", "User Logout", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/layout/AppLayout.tsx"]),
    ("AC-36", "After logout, the user cannot access protected routes without re-authenticating.", "User Logout", "Phase 1: Minimum Viable Product (MVP)", ["client/src/components/layout/AppLayout.tsx"]),
    ("AC-37", "Only content_team_member can access /analytics.", "View Content Performance Metrics", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-38", "Dashboard displays total views, unique visitors, and engagement rate for all content.", "View Content Performance Metrics", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-39", "Metrics are presented in an easy-to-understand visual format (e.g., charts, graphs).", "View Content Performance Metrics", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx", "npm i recharts"]),
    ("AC-40", "User can see performance metrics for individual posts.", "View Content Performance Metrics", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-41", "Only content_team_member can filter analytics data.", "Filter Analytics Data", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-42", "User can select a custom date range to view data.", "Filter Analytics Data", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-43", "User can filter data to show only video posts or text posts.", "Filter Analytics Data", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-44", "Filtered data updates the dashboard in real-time.", "Filter Analytics Data", "Phase 2: Analytics & Integrations", ["client/src/components/analytics/AnalyticsPage.tsx"]),
    ("AC-45", "The data model stores event type and the application uses it as described in this story.", "Filter Analytics Data", "Phase 2: Analytics & Integrations", ["bundle exec rails rhino:blueprint"]),
    ("AC-46", "Only admin can access /admin/integrations.", "Connect to Marketing Tools", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminApiIntegrationsPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-47", "Admin can view a list of available marketing tool integrations (e.g., Mailchimp, HubSpot).", "Connect to Marketing Tools", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminApiIntegrationsPage.tsx"]),
    ("AC-48", "Admin can configure API keys or authentication tokens for selected integrations.", "Connect to Marketing Tools", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminApiIntegrationsPage.tsx"]),
    ("AC-49", "Successful integration is confirmed with a status indicator.", "Connect to Marketing Tools", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminApiIntegrationsPage.tsx"]),
    ("AC-50", "System generates alerts for critical errors (e.g., server downtime, database connection issues).", "System Health Monitoring", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminSystemReportsPage.tsx"]),
    ("AC-51", "System logs application performance metrics (e.g., response times, resource utilization).", "System Health Monitoring", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminSystemReportsPage.tsx"]),
    ("AC-52", "Monitoring data is accessible to admin via a dedicated dashboard (e.g., /admin/monitoring).", "System Health Monitoring", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminSystemReportsPage.tsx", "client/src/routes/custom.jsx"]),
    ("AC-53", "System performs automated daily backups of all application data.", "Data Backup and Restore", "Phase 2: Analytics & Integrations", ["config/schedule.rb"]),
    ("AC-54", "Backup files are stored securely and redundantly.", "Data Backup and Restore", "Phase 2: Analytics & Integrations", ["config/schedule.rb"]),
    ("AC-55", "admin can initiate a data restore process from a recent backup.", "Data Backup and Restore", "Phase 2: Analytics & Integrations", ["client/src/components/admin/AdminSystemSettingsPage.tsx"]),
    ("AC-56", "content_team_member cannot access /admin routes.", "Role-Based Access Control", "Phase 2: Analytics & Integrations", ["client/src/routes/custom.jsx"]),
    ("AC-57", "admin has full access to all application features and data.", "Role-Based Access Control", "Phase 2: Analytics & Integrations", ["server/.rhino/blueprints/_roles.yaml"]),
    ("AC-58", "Unauthorized access attempts are logged and blocked.", "Role-Based Access Control", "Phase 2: Analytics & Integrations", ["client/src/routes/custom.jsx"]),
    ("AC-59", "Extra: Dashboard metrics endpoint for aggregated data", "Custom endpoint", "Phase 2: Analytics & Integrations", ["app/controllers/api/dashboard_controller.rb"]),
    ("AC-60", "Extra: Ensure Users table has correct fields (first_name, last_name, approved, profile_completed)", "Data Model Update", "Phase 1: Minimum Viable Product (MVP)", ["bundle exec rails g migration AddFieldsToUsers approved:boolean profile_completed:boolean first_name:string last_name:string"]),
    ("AC-61", "Extra: Create sample roles and UsersRole in seeds", "Data Seeding", "Phase 1: Minimum Viable Product (MVP)", ["db/seeds.rb"])
]

out = {
    "criteria": [],
    "updated_at": datetime.datetime.now().isoformat() + "Z"
}

for c in criteria:
    out["criteria"].append({
        "id": c[0],
        "name": c[1],
        "user_story": c[2],
        "phase": c[3],
        "status": "pending",
        "subtasks": c[4]
    })
    
with open(".codalio/acceptance-criteria.json", "w") as f:
    json.dump(out, f, indent=2)

