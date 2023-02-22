import datetime
import os
import platform

import psutil
import uptime
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/ping')
def ping():
    return "pong\n"


@app.route('/info')
def get_info():
    data = {
        'date_time': datetime.datetime.now(),
        'machine': {
            'host_name': platform.node(),
            'boot_time': '{}'.format(uptime.boottime()),
            'up_time': '{}'.format(datetime.timedelta(seconds=uptime.uptime())),
            'architecture': platform.architecture()[0],
            'cpu': _get_cpus(),
            'memory': _get_mem(),
        },
        'OS': {
            'platform': platform.platform(),
            'version': platform.version()
        }
    }
    return data


def _get_mem():
    vm = psutil.virtual_memory()
    return {
        'total': '{} GB'.format(round(vm.total / (1024 ** 3))),
        'used': '{} GB'.format(round(vm.used / (1024 ** 3))),
    }


def _get_cpus():
    cpu_freq = psutil.cpu_freq()
    core_usage = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        core_usage.append('{}: {}%'.format(i, percentage))

    return {
        'total_cores': psutil.cpu_count(logical=True),
        'physical cores': psutil.cpu_count(logical=False),
        'frequency': {
            'current': round(cpu_freq.current),
            'min': cpu_freq.min,
            'max': cpu_freq.max,
        },
        'total_usage': psutil.cpu_percent(),
        'cores_usage': core_usage
    }


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)
