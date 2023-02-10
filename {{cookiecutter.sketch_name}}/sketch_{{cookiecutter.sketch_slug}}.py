import vsketch
from shapely.geometry import Point

class {{cookiecutter.class_name}}(vsketch.SketchClass):
    # Sketch parameters:
    debug = vsketch.Param(False)
    width = vsketch.Param(5., decimals=2, unit="in")
    height = vsketch.Param(3., decimals=2, unit="in")
    landscape = vsketch.Param({{cookiecutter.landscape}})
    center = vsketch.Param(True)
    pen_width = vsketch.Param(0.7, decimals=3, min_value=1e-10, unit="mm")
    num_layers = vsketch.Param(1)
    # radius = vsketch.Param(1.0, decimals=3, unit="in")

    def random_point(self, vsk: vsketch.Vsketch):
        return Point(vsk.random(0, self.width), vsk.random(0, self.height))

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(f"{self.height}x{self.width}", landscape=self.landscape, center=self.center)
        vsk.penWidth(f"{self.pen_width}")

        # implement your sketch here
        # layers = [1 + i for i in range(self.num_layers)]
        # layer = layers[int(vsk.random(0, len(layers)))]
        # vsk.stroke(layer)
        # vsk.fill(layer)
        # vsk.circle(0, 0, self.radius, mode="radius")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
