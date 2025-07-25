#!/usr/bin/env bash
socat TCP-LISTEN:1338,reuseaddr,fork EXEC:"/vuln/chall",stderr
