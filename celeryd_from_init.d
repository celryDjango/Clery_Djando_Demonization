CELERY_BIN="/home/venkatesh/.local/bin/celery"

# App instance to use
CELERY_APP="reflection"

# Where to chdir at start.
#CELERYD_CHDIR="/home/venkatesh/PycharmProjects/celeryinpython/"
CELERYD_CHDIR="/home/venkatesh/Documents/reflection/"


# Extra command-line arguments to the worker
CELERYD_OPTS="--time-limit=300 --concurrency=8"

# %n will be replaced with the first part of the nodename.
CELERYD_LOG_FILE="/var/log/celery/%n%I.log"
CELERYD_PID_FILE="/var/run/celery/%n.pid"

# Workers should run as an unprivileged user.
#   You need to create this user manually (or you can choose
#   a user/group combination that already exists (e.g., nobody).
CELERYD_USER="venkatesh"
CELERYD_GROUP="venkatesh"

# If enabled pid and log directories will be created if missing,
# and owned by the userid/group configured.
CELERY_CREATE_DIRS=1

export SECRET_KEY="foobar"
