import vsketch
from shapely.geometry import Point


class {{cookiecutter.class_name}}(vsketch.SketchClass):
    # Sketch parameters:
    debug = vsketch.Param(False)
    width = vsketch.Param(5., decimals=2, unit="in")
    height = vsketch.Param(3., decimals=2, unit="in")
    pen_width = vsketch.Param(0.7, decimals=3, unit="mm")
    num_layers = vsketch.Param(1)

    def random_point(self, vsk: vsketch.Vsketch):
        return Point(vsk.random(0, self.width), vsk.random(0, self.height))

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(f"{self.height}x{self.width}", landscape={{cookiecutter.landscape}}, center=False)
        vsk.penWidth(f"{self.pen_width}")

        layers = [1 + i for i in range(self.num_layers)]
        # implement your sketch here
        # layer = layers[math.floor(vsk.random(0, len(layers)))]
        # vsk.stroke(layer)
        # vsk.circle(0, 0, self.radius, mode="radius")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
