# fix the typo in the config file
exec { 'replace':
command	=> "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
path	=> '/bin',
}
