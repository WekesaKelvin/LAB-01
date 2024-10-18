import cairo
import math
import constraints


surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 600)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

context.set_line_width(3)
context.rectangle(100,560,600,20)
context.set_source_rgb(0,0,0)
context.stroke()

context.move_to(110,560)
context.line_to(110,348)
context.set_source_rgb(0,0,0)
context.stroke()

context.move_to(320,560)
context.line_to(320,348)
context.set_source_rgb(0,0,0)
context.stroke()

context.move_to(690,560)
context.line_to(690,345)
context.set_source_rgb(0,0,0)
context.stroke()

context.rectangle(140, 410, 150, 100)
context.set_source_rgb(0, 0, 0)
context.stroke()
context.rectangle(130, 510, 170, 10)
context.set_source_rgb(0, 0, 0)
context.stroke()

context.rectangle(480, 410, 150, 100)
context.set_source_rgb(0, 0, 0)
context.stroke()
context.rectangle(470, 510, 170, 10)
context.set_source_rgb(0, 0, 0)
context.stroke()

context.move_to(95, 365)
context.line_to(215, 245)
context.line_to(335, 365)
context.move_to(80, 350)
context.line_to(215, 220)
context.line_to(350, 350)
context.move_to(95, 365)
context.line_to(80, 350)
context.move_to(335, 365)
context.line_to(350, 350)
context.set_source_rgb(0, 0, 0)
context.stroke()

context.move_to(345, 345)
context.line_to(720, 345)
context.move_to(245, 250)
context.line_to(620, 250)
context.line_to(720, 345)
context.stroke()

# Start of crescent
context.set_line_width(3)
context.arc(650, 100, 40, 6.5*math.pi/4, math.pi/1.1)
context.curve_to(650, 120, 680, 80, 664, 60)
context.set_source_rgb(1,1,1)
context.fill_preserve()
context.set_source_rgb(0,0,0)
context.stroke()

context.set_line_width(3)
context.rectangle(180,300,60,60)
context.set_source_rgb(0,0,0)
context.stroke()


surface.write_to_png(f'{constraints.OUTPUT_DIR}house.png')