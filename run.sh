# Reason for "-nolisten tcp", not documented within Xvfb manpages (for who knows what reason)
# https://superuser.com/questions/855019/make-xvfb-listen-only-on-local-ip
Xvfb :99 -screen 0 1024x768x24 -nolisten tcp
