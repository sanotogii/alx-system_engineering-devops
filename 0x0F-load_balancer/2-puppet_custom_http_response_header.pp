# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create a custom Nginx configuration file for the custom header
file { 'header_served_by':
  path  => '/etc/nginx/sites-available/default',
  match => '^server {',
  line  => "server {\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,

# Restart Nginx service to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}
