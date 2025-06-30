#!/usr/bin/env bash
socat TCP-LISTEN:1337,fork EXEC:/vuln/chall,pty,stderr