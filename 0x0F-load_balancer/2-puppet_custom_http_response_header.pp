# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create a custom Nginx configuration file for the custom header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

# Restart Nginx service to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}
