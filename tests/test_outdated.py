#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from typer.testing import CliRunner

from gvsbuild.main import app

runner = CliRunner()


def test_outdated():
    result = runner.invoke(app, ["outdated", "--help"])
    assert result.exit_code == 0
    assert "--help" in result.stdout


def test_extra_arg():
    result = runner.invoke(app, ["outdated", "extra"])
    assert result.exit_code == 2
    assert "Got unexpected extra" in result.stdout
