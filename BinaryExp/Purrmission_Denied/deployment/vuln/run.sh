#!/usr/bin/env bash
socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/vuln/chall",stderr
