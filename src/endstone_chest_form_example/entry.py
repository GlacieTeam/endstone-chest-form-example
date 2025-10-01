# MIT License
#
# Copyright (c) 2025 GlacieTeam
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from endstone.plugin import Plugin
from endstone.command import CommandSender, Command
from endstone import Player

# import and use chest_form_api_endstone package
from chest_form_api_endstone import ChestForm


class Entry(Plugin):
    prefix = "ChestFormExample"
    api_version = "0.10"
    load = "POSTWORLD"
    commands = {
        "chest": {
            "description": "Open chest form.",
            "usages": ["/chest"],
        }
    }

    def on_enable(self):
        self.logger.info("ChestFormExample loaded!")

    def on_command(self, sender: CommandSender, command: Command, _):
        match command.name:
            case "chest":
                if isinstance(sender, Player):
                    form = ChestForm(self, "Example Chest Form")
                    form.fill_slots(
                        "minecraft:bedrock",
                        display_name=" ",
                    )

                    def call_back(player: Player, index: int):
                        player.send_message(
                            f"You clicked the chest form button, button index {index}"
                        )
                        form.send_to(player)

                    form.set_slot(
                        12,
                        "minecraft:diamond_block",
                        call_back,
                        display_name="Test Button",
                        lore=["1111", "22222"],
                        enchants={"protection": 114, "sharpness": 514},
                    )
                    form.send_to(sender)
                else:
                    sender.send_error_message(
                        "This command can only be executed by player."
                    )
                return False
        return True
