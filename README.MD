# Stress tests

## Installation

`chmod +x ./installation/*`

`./installation/with_yum.sh` or `./installation/with_apt.sh`

## Testing

`locust -f ./tests/<platform>.py`

platform = firebase/parse/appbase

Goto _localhost:8089_.