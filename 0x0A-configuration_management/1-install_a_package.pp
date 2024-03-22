# install flask from pip3 with puppet
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}

file { '/usr/local/bin/flask':
  ensure => link,
  target => '/usr/local/bin/flask',
  require => Exec['install_flask'],
}

