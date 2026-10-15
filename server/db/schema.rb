# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[8.1].define(version: 2026_10_15_151012) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "pg_catalog.plpgsql"

  create_table "analytics_data", force: :cascade do |t|
    t.bigint "organization_id", null: false
    t.string "event_type"
    t.json "event_data"
    t.datetime "recorded_at"
    t.bigint "post_id"
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_analytics_data_on_discarded_at"
    t.index ["organization_id"], name: "index_analytics_data_on_organization_id"
    t.index ["post_id"], name: "index_analytics_data_on_post_id"
  end

  create_table "audit_logs", force: :cascade do |t|
    t.string "auditable_type", null: false
    t.bigint "auditable_id", null: false
    t.string "action", null: false
    t.json "old_values"
    t.json "new_values"
    t.bigint "user_id"
    t.string "user_type"
    t.string "ip_address"
    t.string "user_agent"
    t.bigint "organization_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["action"], name: "index_audit_logs_on_action"
    t.index ["auditable_type", "auditable_id"], name: "index_audit_logs_on_auditable_type_and_auditable_id"
    t.index ["created_at"], name: "index_audit_logs_on_created_at"
    t.index ["organization_id"], name: "index_audit_logs_on_organization_id"
    t.index ["user_id"], name: "index_audit_logs_on_user_id"
  end

  create_table "org_role_permissions", force: :cascade do |t|
    t.bigint "organization_id", null: false
    t.bigint "role_id", null: false
    t.json "permissions", default: []
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["organization_id", "role_id"], name: "index_org_role_permissions_on_org_role", unique: true
    t.index ["organization_id"], name: "index_org_role_permissions_on_organization_id"
    t.index ["role_id"], name: "index_org_role_permissions_on_role_id"
  end

  create_table "organizations", force: :cascade do |t|
    t.string "name", null: false
    t.string "slug", null: false
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["slug"], name: "index_organizations_on_slug", unique: true
  end

  create_table "posts", force: :cascade do |t|
    t.bigint "organization_id", null: false
    t.string "title"
    t.text "content"
    t.string "status", default: "draft"
    t.datetime "published_at"
    t.bigint "user_id"
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_posts_on_discarded_at"
    t.index ["organization_id"], name: "index_posts_on_organization_id"
    t.index ["user_id"], name: "index_posts_on_user_id"
  end

  create_table "roles", force: :cascade do |t|
    t.string "name", null: false
    t.string "slug", null: false
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["slug"], name: "index_roles_on_slug", unique: true
  end

  create_table "user_roles", force: :cascade do |t|
    t.bigint "user_id", null: false
    t.bigint "organization_id"
    t.bigint "role_id", null: false
    t.string "route_group"
    t.json "permissions", default: []
    t.json "granted_permissions", default: []
    t.json "denied_permissions", default: []
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index "user_id, COALESCE(organization_id, (0)::bigint), role_id, COALESCE(route_group, ''::character varying)", name: "index_user_roles_on_user_org_role_group", unique: true
    t.index ["organization_id"], name: "index_user_roles_on_organization_id"
    t.index ["role_id"], name: "index_user_roles_on_role_id"
    t.index ["user_id"], name: "index_user_roles_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "name", null: false
    t.string "email", null: false
    t.string "password_digest", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "api_token"
    t.boolean "approved"
    t.boolean "profile_completed"
    t.string "first_name"
    t.string "last_name"
    t.string "invitation_token"
    t.index ["api_token"], name: "index_users_on_api_token", unique: true
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["invitation_token"], name: "index_users_on_invitation_token", unique: true
  end

  create_table "videos", force: :cascade do |t|
    t.bigint "organization_id", null: false
    t.string "title"
    t.string "url"
    t.integer "duration"
    t.bigint "post_id"
    t.bigint "user_id"
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_videos_on_discarded_at"
    t.index ["organization_id"], name: "index_videos_on_organization_id"
    t.index ["post_id"], name: "index_videos_on_post_id"
    t.index ["user_id"], name: "index_videos_on_user_id"
  end

  add_foreign_key "analytics_data", "organizations"
  add_foreign_key "analytics_data", "posts"
  add_foreign_key "org_role_permissions", "organizations"
  add_foreign_key "org_role_permissions", "roles"
  add_foreign_key "posts", "organizations"
  add_foreign_key "posts", "users"
  add_foreign_key "user_roles", "organizations"
  add_foreign_key "user_roles", "roles"
  add_foreign_key "user_roles", "users"
  add_foreign_key "videos", "organizations"
  add_foreign_key "videos", "posts"
  add_foreign_key "videos", "users"
end
