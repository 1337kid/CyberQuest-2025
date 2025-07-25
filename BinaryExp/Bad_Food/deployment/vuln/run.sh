#!/usr/bin/env bash
socat TCP-LISTEN:1336,reuseaddr,fork EXEC:"/vuln/chall",stderr
