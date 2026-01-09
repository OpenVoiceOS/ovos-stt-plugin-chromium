#!/usr/bin/env python3
import os

from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-stt-plugin-chromium = ovos_stt_plugin_chromium:ChromiumSTT'
CONFIG_ENTRY_POINT = 'ovos-stt-plugin-chromium.config = ovos_stt_plugin_chromium:ChromiumSTTConfig'

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """ Find the version of the package"""
    version_file = f'{BASEDIR}/ovos_stt_plugin_chromium/version.py'
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    return version


setup(
    name='ovos-stt-plugin-chromium',
    version=get_version(),
    description='A stt plugin for OVOS using the google chrome browser api',
    url='https://github.com/OpenVoiceOS/ovos-stt-plugin-chromium',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_stt_plugin_chromium'],
    install_requires=["requests",
                      "ovos_utils>=0.0.12",
                      "ovos-plugin-manager>=0.0.1"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='mycroft ovos plugin stt',
    entry_points={'opm.stt': PLUGIN_ENTRY_POINT,
                  'opm.stt.config': CONFIG_ENTRY_POINT}
)
