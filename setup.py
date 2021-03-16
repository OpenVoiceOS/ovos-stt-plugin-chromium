#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'chromium_stt_plug = jarbas_stt_plugin_chromium:ChromiumSTT'
setup(
    name='jarbas-stt-plugin-chromium',
    version='0.2.0',
    description='A stt plugin for mycroft using the google chrome browser api',
    url='https://github.com/JarbasLingua/jarbas-stt-plugin-chromium',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['jarbas_stt_plugin_chromium'],
    install_requires=["requests", "ovos_utils>=0.0.8a3"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin stt',
    entry_points={'mycroft.plugin.stt': PLUGIN_ENTRY_POINT}
)
