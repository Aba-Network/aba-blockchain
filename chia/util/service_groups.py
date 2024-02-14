# Aba has modified this file
from __future__ import annotations

from typing import Generator, Iterable, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "aba_harvester",
        "aba_timelord_launcher",
        "aba_timelord",
        "aba_farmer",
        "aba_full_node",
        "aba_wallet",
        "aba_data_layer",
        "aba_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["aba_wallet", "aba_data_layer"],
    "data_layer_http": ["aba_data_layer_http"],
    "node": ["aba_full_node"],
    "harvester": ["aba_harvester"],
    "farmer": ["aba_harvester", "aba_farmer", "aba_full_node", "aba_wallet"],
    "farmer-no-wallet": ["aba_harvester", "aba_farmer", "aba_full_node"],
    "farmer-only": ["aba_farmer"],
    "timelord": ["aba_timelord_launcher", "aba_timelord", "aba_full_node"],
    "timelord-only": ["aba_timelord"],
    "timelord-launcher-only": ["aba_timelord_launcher"],
    "wallet": ["aba_wallet"],
    "introducer": ["aba_introducer"],
    "simulator": ["aba_full_node_simulator"],
    "crawler": ["aba_crawler"],
    "seeder": ["aba_crawler", "aba_seeder"],
    "seeder-only": ["aba_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups: Iterable[str]) -> Generator[str, None, None]:
    for group in groups:
        yield from SERVICES_FOR_GROUP[group]


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
