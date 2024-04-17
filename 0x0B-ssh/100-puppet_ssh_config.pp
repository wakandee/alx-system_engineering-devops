#!/usr/bin/env bash
#using puppet to make changes to our config file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentiFile ~/.ssh/school
	PasswordAuthentication no
",
}
