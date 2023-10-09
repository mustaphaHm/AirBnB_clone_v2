#!/usr/bin/env bash
# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
	    apt-get update
	        apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
	    rm -f /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
alias_line="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name _;/a $alias_line" $config_file

# Restart Nginx
service nginx restart

exit 0
