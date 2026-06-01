#!/usr/bin/env python3
import yaml

matrix = []


def add(version, config):
    """Add build combinations to the matrix.
    
    Args:
        version (str): Caddy version
        config (dict): Dictionary containing stability, go version and supported OSes
            Format: {
                "version": "2.x.x",
                "stability": "stable|oldstable|next",
                "go_version": "1.x.x",
                "oses": ["debian-11", "ubuntu-22.04", etc...],
                "xcaddy_version": "0.x.x",
                "mod_security_version": "1.x.x",
                "mod_l4_version": "1.x.x",
                "mod_crowdsec_bouncer_version": "0.x.x",
                "mod_cache_handler_version": "0.x.x",
                "mod_libdns_version": "1.x.x",
                "mod_dynamicdns_version": "1.x.x",
                "mod_cloudflare_version": "1.x.x",
                "mod_webdav_version": "1.x.x",
                "mod_defender_version": "0.x.x",
                "mod_ratelimit_version": "0.x.x",
                "mod_fail2ban_version": "0.x.x",
            }
    """
    caddy_version = config.get("version", version)

    for os in config["oses"]:
        matrix.append({
            "caddy_version": caddy_version,
            "stability": config["stability"],
            "go_version": config["go_version"],
            "os": os,
            "xcaddy_version": config["xcaddy_version"],
            "mod_security_version": config["mod_security_version"],
            "mod_l4_version": config["mod_l4_version"],
            "mod_crowdsec_bouncer_version": config["mod_crowdsec_bouncer_version"],
            "mod_libdns_version": config["mod_libdns_version"],
            "mod_dynamicdns_version": config["mod_dynamicdns_version"],
            "mod_cloudflare_version": config["mod_cloudflare_version"],
            "mod_webdav_version": config["mod_webdav_version"],
            "mod_defender_version": config["mod_defender_version"],
            "mod_ratelimit_version": config["mod_ratelimit_version"],
            "mod_fail2ban_version": config["mod_fail2ban_version"],
            "mod_cache_handler_version": config["mod_cache_handler_version"],
            "mod_certmagic_version": config.get("mod_certmagic_version", ""),
            "enabled_modules": " ".join(config["enabled_modules"]),
        })

CADDY_CONFIGS = {
    # Caddy 2.11.3 — cible unique (caddy-l4@master requires v2.11.3+)
    # trixie + noble = stable ; forky = next
    "2.11.3-stable": {
        "version": "2.11.3",
        "stability": "stable",
        "go_version": "1.25.0",
        # Debian 13 (trixie) + Ubuntu 24.04 (noble)
        "oses": ["debian-13", "ubuntu-24.04"],
        "xcaddy_version": "0.4.4",
        "mod_security_version": "v1.1.21",
        # v0.1.1 pins github.com/caddyserver/caddy/v2 v2.11.3
        "mod_l4_version": "v0.1.1",
        "mod_crowdsec_bouncer_version": "v0.2.0",
        # Caddy 2.11.3 requires libdns >= v1.1.1
        "mod_libdns_version": "v1.1.1",
        "mod_dynamicdns_version": "b846b9e8fb83f52be540fb7876116f944e56d551",
        "mod_certmagic_version": "v0.25.3",
        "mod_cloudflare_version": "35fb8474f57d7476329f75d63eebafb95a93022f",
        "mod_webdav_version": "42168ba04c9dc2cd228ab8c453dbab27654e52e6",
        "mod_defender_version": "85fdeb25b6250e31b8e38669c642ca703b007b7f",
        "mod_ratelimit_version": "a8e9f68d7bedc7ddb0c5bb93d6d32d8cf75fcc9f",
        "mod_fail2ban_version": "c4139952edefb952b7b2e11d921be227ae9da501",
        "mod_cache_handler_version": "v0.15.0",
        "enabled_modules": [
            "caddy_exec",
            "caddy_security",
            "caddy_l4",
            "caddy_crowdsec_bouncer",
            "caddy_webdav",
            "caddy_ratelimit",
            "cache_handler",
            "caddy_fail2ban",
            "caddy_cloudflare",
            "caddy_defender",
            "caddy_certmagic",
            "caddy_libdns",
            "caddy_dynamicdns",
            "caddy_replace_response",
        ],
    },
    "2.11.3-next": {
        "version": "2.11.3",
        "stability": "next",
        "go_version": "1.25.0",
        # Debian testing (forky)
        "oses": ["debian-testing"],
        "xcaddy_version": "0.4.4",
        "mod_security_version": "v1.1.21",
        "mod_l4_version": "v0.1.1",
        "mod_crowdsec_bouncer_version": "v0.2.0",
        # Caddy 2.11.3 requires libdns >= v1.1.1
        "mod_libdns_version": "v1.1.1",
        "mod_dynamicdns_version": "b846b9e8fb83f52be540fb7876116f944e56d551",
        "mod_certmagic_version": "v0.25.3",
        "mod_cloudflare_version": "35fb8474f57d7476329f75d63eebafb95a93022f",
        "mod_webdav_version": "42168ba04c9dc2cd228ab8c453dbab27654e52e6",
        "mod_defender_version": "85fdeb25b6250e31b8e38669c642ca703b007b7f",
        "mod_ratelimit_version": "a8e9f68d7bedc7ddb0c5bb93d6d32d8cf75fcc9f",
        "mod_fail2ban_version": "c4139952edefb952b7b2e11d921be227ae9da501",
        "mod_cache_handler_version": "v0.15.0",
        "enabled_modules": [
            "caddy_exec",
            "caddy_security",
            "caddy_l4",
            "caddy_crowdsec_bouncer",
            "caddy_webdav",
            "caddy_ratelimit",
            "cache_handler",
            "caddy_fail2ban",
            "caddy_cloudflare",
            "caddy_defender",
            "caddy_certmagic",
            "caddy_libdns",
            "caddy_dynamicdns",
            "caddy_replace_response",
        ],
    },
}

for version, config in CADDY_CONFIGS.items():
    add(version, config)

print(yaml.safe_dump({ "include": matrix }, sort_keys=False)) 
