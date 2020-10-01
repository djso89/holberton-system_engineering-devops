# fix the typo in the config file
exec { '/usr/bin/env sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
