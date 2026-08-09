# caddy-builds

This repository contains automated builds of [Caddy](https://github.com/caddyserver/caddy) for various Linux distributions. The builds are provided as Debian packages (.deb) and include additional plugins for enhanced functionality.

## Available Packages

For each version of Caddy, we provide a single package:
- `caddy_{version}_{distro}_{arch}.deb`: Caddy binary with additional plugins

## Supported Distributions

- Ubuntu:
  - 22.04 (Jammy)
  - 24.04 (Noble)
- Debian:
  - 11 (Bullseye)
  - 12 (Bookworm)

## Included Plugins

The builds include different sets of plugins depending on the Caddy version:

### Base Plugins (All Versions)
These plugins are included in all Caddy versions:
- [caddy-exec](https://github.com/abiosoft/caddy-exec): Execute commands on Caddy events
- [caddy-security](https://github.com/greenpau/caddy-security): Security features for Caddy
- [caddy-l4](https://github.com/mholt/caddy-l4): Layer 4 (TCP/UDP) support
- [caddy-crowdsec-bouncer](https://github.com/hslatman/caddy-crowdsec-bouncer): CrowdSec integration
- [caddy-webdav](https://github.com/mholt/caddy-webdav): WebDAV support
- [caddy-ratelimit](https://github.com/mholt/caddy-ratelimit): Rate limiting
- [cache-handler](https://github.com/caddyserver/cache-handler): Response caching

### Additional Plugins for Caddy ≥ 2.7.6
- [caddy-fail2ban](https://github.com/Javex/caddy-fail2ban): Fail2ban integration
- [caddy-cloudflare](https://github.com/caddy-dns/cloudflare): Cloudflare DNS support

### Additional Plugins for Caddy ≥ 2.9.1
- [caddy-defender](https://github.com/jasonlovesdoggo/caddy-defender): Security features
- [caddy-certmagic](https://github.com/caddyserver/certmagic): Certificate management

### Additional Plugins for Caddy ≥ 2.10.0
- [caddy-libdns](https://github.com/libdns/libdns): DNS provider library
- [caddy-dynamicdns](https://github.com/mholt/caddy-dynamicdns): Dynamic DNS support

## Installation

### Manual Installation

1. Download the appropriate .deb file for your distribution from the [Releases](https://github.com/krate-apps/caddy-builds/releases) page.
2. Install the package using:
   ```bash
   sudo dpkg -i caddy_{version}_{distro}_{arch}.deb
   ```
3. Fix any dependencies if needed:
   ```bash
   sudo apt-get install -f
   ```

## Build Information

### The JSON Metadata

Each package comes with a JSON metadata file that can be used for automated installations. The metadata includes:
- Package name
- Version
- Distribution codename
- Dependencies
- Installation instructions

### Dependencies

The packages are built with the following dependencies:
- Go ${go_version}
- xcaddy (latest)
- UPX for binary compression

### Build Configuration

The packages are built using xcaddy with a version-specific configuration. The build process is automated through GitHub Actions and includes:

1. **Build Environment**:
   - Go version specified in the version matrix
   - xcaddy for building Caddy with plugins
   - UPX for binary compression
   - Required build dependencies

2. **Build Process**:
   - Binary compilation with specific plugin versions
   - Symbol stripping for reduced size
   - UPX compression for optimal binary size
   - Package creation with proper metadata

3. **Configuration Management**:
   - Version-specific plugin inclusion (see Included Plugins section)
   - Module version management through matrix.py
   - Distribution-specific builds
   - Automated metadata generation

The exact configuration for each Caddy version can be found in the [matrix.py](matrix.py) file, which defines:
- Module versions
- Enabled plugins
- Build dependencies
- Supported distributions

### Build Metadata

Each package in the release assets is accompanied by a JSON metadata file (e.g., `caddy_2.10.0_debian-bookworm_amd64.json`) that contains detailed information about how the package was built:

```json
{
  "package_id": "caddy_2.10.0_debian-bookworm_amd64",
  "version": "2.10.0",
  "build": "1build1",
  "checksum_sha256": "6e59d8449cff20cdd60aa132473e2b18be60287afc20d59fd02153bda8268750",
  "build_date": "2025-06-08T17:09:59Z",
  "category": "caddy",
  "tag": "next",
  "type": "bin",
  "os": "bookworm",
  "go_version": "1.24.3",
  "xcaddy_version": "0.4.4",
  "enabled_plugins": "caddy-exec,caddy-security,caddy-l4,caddy-crowdsec-bouncer,caddy-webdav,caddy-ratelimit,cache-handler,caddy-fail2ban,caddy-cloudflare,caddy-defender,caddy-certmagic,caddy-libdns,caddy-dynamicdns",
  "caddy_exec_version": "rev=",
  "caddy_security_version": "v1.1.21",
  "caddy_l4_version": "rev=4d3c80e89c5f80438a3e048a410d5543ff5fb9f4",
  "caddy_crowdsec_bouncer_version": "v0.2.0",
  "caddy_webdav_version": "rev=42168ba04c9dc2cd228ab8c453dbab27654e52e6",
  "caddy_ratelimit_version": "rev=a8e9f68d7bedc7ddb0c5bb93d6d32d8cf75fcc9f",
  "cache_handler_version": "",
  "caddy_fail2ban_version": "rev=c4139952edefb952b7b2e11d921be227ae9da501",
  "caddy_cloudflare_version": "rev=35fb8474f57d7476329f75d63eebafb95a93022f",
  "caddy_defender_version": "rev=85fdeb25b6250e31b8e38669c642ca703b007b7f",
  "caddy_certmagic_version": "rev=",
  "caddy_libdns_version": "rev=6be57668e7bf10f6c31ab7ffcd7cc132766c1ee2",
  "caddy_dynamicdns_version": "rev=b846b9e8fb83f52be540fb7876116f944e56d551"
}
```

This metadata file provides:
- Package identification and versioning
- Build information (date, checksum, build number)
- Complete list of enabled plugins
- Exact version of each plugin (including commit hashes)
- Go and xcaddy versions used for the build
- Target distribution information

You can use this metadata to:
- Verify the exact configuration of any package
- Reproduce the build environment
- Check which plugins are included
- See the exact versions of all components
- Validate package integrity using checksums

## Version Matrix

| Caddy Version | Go Version | Ubuntu | Debian |
|---------------|------------|---------|---------|
| 2.10.0 | 1.24.3 | 22.04, 24.04 | 11, 12 |
| 2.9.0 | 1.24.3 | 22.04, 24.04 | 11, 12 |
| 2.8.4 | 1.24.3 | 22.04, 24.04 | 11, 12 |
| 2.7.6 | 1.24.3 | 22.04, 24.04 | 11, 12 |
| 2.6.4 | 1.24.3 | 22.04, 24.04 | 11, 12 |
| 2.5.2 | 1.24.3 | 22.04, 24.04 | 11, 12 |

## Binary Optimization

Each Caddy binary is optimized using:
- `strip --strip-unneeded`: Removes unnecessary symbols
- `upx --best --lzma`: Compresses the binary using UPX with LZMA compression

## License

Caddy is distributed under the [Apache License 2.0](https://github.com/caddyserver/caddy/blob/master/LICENSE). 
