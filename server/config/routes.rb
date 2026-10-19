Rails.application.routes.draw do
  get "up" => "rails/health#show", as: :rails_health_check

  scope 'api/:organization', defaults: { route_group: 'tenant' } do
    get 'dashboard/stats', to: 'api/dashboard#stats'
  end
end
