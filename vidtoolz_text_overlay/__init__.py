import vidtoolz
import subprocess
import tempfile
import os
import sys
from typing import List

DEFAULT_FONT      = "DejaVu-Sans-Bold"   # will be located automatically
DEFAULT_FONTSIZE  = 48
DEFAULT_COLOR     = "white"
DEFAULT_BORDER_W  = 2
DEFAULT_BORDER_C  = "black"
DEFAULT_CODEC     = "libx264"
DEFAULT_PRESET    = "veryfast"
DEFAULT_CRF       = 18

def create_parser(subparser):
    p = subparser.add_parser("otext", description="Add text overlay on video using ffmpeg")
    # Add subprser arguments here.
    p.add_argument("input",  help="input video file")
    p.add_argument("output", help="output video file")

    # ---- shared defaults ----------------------------------------------------
    p.add_argument("--font",      default=DEFAULT_FONT,
                   help=f"font family or .ttf/.otf file (default: {DEFAULT_FONT})")
    p.add_argument("--fontsize",  type=int, default=DEFAULT_FONTSIZE)
    p.add_argument("--color",     default=DEFAULT_COLOR,
                   help=f"font colour (default: {DEFAULT_COLOR})")
    p.add_argument("--borderw",   type=int, default=DEFAULT_BORDER_W,
                   help=f"text border width (default: {DEFAULT_BORDER_W})")
    p.add_argument("--borderc",   default=DEFAULT_BORDER_C,
                   help=f"text border colour (default: {DEFAULT_BORDER_C})")

    # ---- codec choices ------------------------------------------------------
    p.add_argument("--vcodec",    default=DEFAULT_CODEC,
                   help=f"video codec (default: {DEFAULT_CODEC})")
    p.add_argument("--preset",    default=DEFAULT_PRESET,
                   help=f"x264 preset (default: {DEFAULT_PRESET})")
    p.add_argument("--crf",       type=int, default=DEFAULT_CRF,
                   help=f"CRF quality 0-51, lower=better (default: {DEFAULT_CRF})")

    # ---- per-overlay arguments ---------------------------------------------
    # Each use of --text may be followed by these scoped options
    text_group = p.add_argument_group("Per-overlay options (repeatable)")
    text_group.add_argument("--text",    action="append", required=True,
                            help="text string (repeat as needed)")
    text_group.add_argument("--start",   action="append", type=float,
                            help="start time in seconds (repeat or use default)")
    text_group.add_argument("--dur",     action="append", type=float,
                            help="duration in seconds (repeat or use default)")
    text_group.add_argument("--x",       action="append",
                            help="x position: number, 'center', 'left', 'right'")
    text_group.add_argument("--y",       action="append",
                            help="y position: number, 'center', 'top', 'bottom'")
    return p


class ViztoolzPlugin:
    """ Add text overlay on video using ffmpeg """
    __name__ = "otext"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        pass

    def hello(self, args):
        # this routine will be called when "vidtoolz "otext is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")

otext_plugin = ViztoolzPlugin()
