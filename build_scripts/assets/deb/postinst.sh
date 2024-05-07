#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/aba/resources/app.asar.unpacked/daemon/aba /usr/bin/aba || true
ln -s /opt/aba/aba-blockchain /usr/bin/aba-blockchain || true
