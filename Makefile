run_server:
	gunicorn --workers=4 --log-level debug -b 0.0.0.0:${PORT} app:app