# basic_isaac_sim_project

A modular Isaac Sim project template for building single-scene and multi-environment simulation scripts.

## Structure

- `config/`: project constants and default configuration
- `core/`: stage, app, physics, lights, materials, transforms
- `assets/`: official NVIDIA asset helpers and registry
- `environments/`: environment shell loaders
- `robots/`: robot loaders and fleet definitions
- `props/`: warehouse, office, hospital, terrain, and generic props
- `tasks/`: task metadata and scenario goals
- `scenes/`: scene builders
- `examples/`: runnable entry scripts
- `utils/`: utility helpers

## Notes

This template is designed for:
- Isaac Sim Script Editor usage
- scene generation with built-in NVIDIA assets
- easy extension into custom research/demo repositories

The code is intentionally modular so you can reuse the same building blocks across many scenes.
