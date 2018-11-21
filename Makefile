deploy:
	scp index.py root@207.154.233.91:~/britecore-test; \
	scp setup.py root@207.154.233.91:~/britecore-test; \
	scp templates/index.html root@207.154.233.91:~/britecore-test/templates; \
	ssh root@207.154.233.91 "systemctl restart flaskapp.service"
