# install flask from pip3 with puppet
package {'python3-pip':
ensure  => 'installed',
}
exec { 'install_werkzeug':
command => '/usr/bin/pip3 install Werkzeug==2.1.1',
path    => '/usr/local/bin:/usr/bin',
require => Package['python3-pip'],
}

exec{ 'install_flask':
command =>  '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/local/bin:/usr/bin',
require => Exec['install_werkzeug'],
}

