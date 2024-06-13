# scaling up the traffic nginx can recieve

exec {'inc':
	path => '/usr/local/bin/:/bin/',
	command => 'sed -i "s/15/8000/" /etc/default/nginx && sudo service nginx restart'
	}
