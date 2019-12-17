import time
import dotmvw as dm

# ------------------------------------------------------------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------------------------------------------------------------

a = time.time()

# ------------------------------------------------------------------------------------------------------------------
# Add and modify pages to session
# ------------------------------------------------------------------------------------------------------------------


gui1 = 'HyperWorks'
version1 = '19'
graphics1 = ['C:/Users/Yumitomo/Projects/HyperWorks/mv_hv_hg/mv_hv_hg/animation/bezel_iter2.h3d']
results1 = ['C:/Users/Yumitomo/Projects/HyperWorks/mv_hv_hg/mv_hv_hg/animation/bezel_iter2.h3d']

pages_state = dm.PageState(gui1, version1, graphics1, results1)
pages_root = dm.Page(pages_state)

pages = pages_root.add_pages(1)  # add pages to session root

pages_state.title = (pages[0].Title, 'Renamed to THIS!')  # change title of specified page
pages_state.animator = (pages[0].Animator, 'Static')  # Change animation type of specified page
pages_state.titlefont = (pages[0].TitleFont, ('Noto Sans', 1, 0, 12))  # change font of title of specified page

# ------------------------------------------------------------------------------------------------------------------
# Add and modify windows to pages
# ------------------------------------------------------------------------------------------------------------------

windows_state = dm.WindowState()  # initialize a state object for all windows of all pages
windows_root = dm.Window(windows_state)  # initialize a root object for all windows of all pages

page0_root = pages[0].Root
windows = windows_root.add_windows(1, page0_root, 1)

# ------------------------------------------------------------------------------------------------------------------
# Add and modify graphics to windows
# ------------------------------------------------------------------------------------------------------------------

graphics_state = dm.GraphicState()  # initialize a graphics state object for all graphics on all windows and pages
graphics_root = dm.Graphic(graphics_state)  # initialize graphics root object for all graphics on all windows and pages

window0_root = windows[0].Root  # get window 0 root node
window0_graphics = graphics_root.add_graphics(1, window0_root)  # add 1 graphic to window 0 root node

# ------------------------------------------------------------------------------------------------------------------
# Add and modify models to graphics
# ------------------------------------------------------------------------------------------------------------------

models_state = dm.ModelState()
models_root = dm.Model(models_state)

window0_graphic0_root = window0_graphics[0].Root  # get graphic 0 root node
window0_graphic0_models = models_root.add_model(1, window0_graphic0_root)  # add 1 model to graphic 0 root node

models_state.scale = (window0_graphic0_models[0].Scale, '1000, 1000, 1000')
# ------------------------------------------------------------------------------------------------------------------
# Add and modify results to models
# ------------------------------------------------------------------------------------------------------------------

results_state = dm.ResultState()
results_root = dm.Result(results_state)

model0_root = window0_graphic0_models[0].Root  # get model 0 root
model0_results = results_root.add_result(1, model0_root)  # add 1 result to model 0 root

results_state.currentsubcase = (model0_results[0].CurrentSubcase, '1, 0')  # change subcase to step 1, increment 0

# ------------------------------------------------------------------------------------------------------------------
# Add and modify parts to models
# ------------------------------------------------------------------------------------------------------------------

parts_state = dm.PartState()
parts_root = dm.Part(parts_state)

model0_root = window0_graphic0_models[0].Root
model0_parts = parts_root.add_part(2, model0_root)

# ------------------------------------------------------------------------------------------------------------------
# Add and modify groups to models
# ------------------------------------------------------------------------------------------------------------------

groups_state = dm.GroupState()  # initialize a groups state object for all groups on all graphics, windows, and pages
groups_root = dm.Group(groups_state)  # initialize groups root object for all groups on all graphics, windows, and pages

model0_root = window0_graphic0_models[0].Root  # get model 0 root
model0_groups_1d = groups_root.add_group(1, 1, model0_root)  # add 1 1d group to model 0
model0_groups_2d = groups_root.add_group(1, 2, model0_root)  # add 1 2d group to model 0

# ------------------------------------------------------------------------------------------------------------------
# Add and modify contours to models
# ------------------------------------------------------------------------------------------------------------------

contours_state = dm.ContourState()  # initialize a contours state object for all contours on all graphics, windows, and pages
contours_root = dm.Contour(contours_state)  # initialize contours root object for all contours on all graphics, windows, and pages

model0_root = window0_graphic0_models[0].Root  # get model 0 root

model0_contours = contours_root.add_contour(1, model0_root) #default result type is displacement
contours_state.datacomponent = (model0_contours[0].DataComponent, 'Y')
contours_state.multiplelayers = (model0_contours[0].MultipleLayers, 'true')
contours_state.averageacrossparts = (model0_contours[0].AverageAcrossParts, 'On')
# model0_contours = contours_root.add_contour(1, model0_root, resulttype='Element Stresses (2D & 3D)', datacomponent='vonMises')

# ------------------------------------------------------------------------------------------------------------------
# Add and modify legends to contours
# ------------------------------------------------------------------------------------------------------------------

legends_state = dm.LegendState()  # initialize a legends state object for all legends on all graphics, windows, and pages
legends_root = dm.Legend(legends_state)  # initialize legends root object for all legends on all graphics, windows, and pages

contour0_root = model0_contours[0].Root
contour0_legends = legends_root.add_legend(1, contour0_root)  # default result type is displacement

legends_state.numcols = (contour0_legends[0].NumCols, '9')
legends_state.noresultcolor = (contour0_legends[0].NoResultColor, '0, 0, 0')
legends_state.legendminthreshold = (contour0_legends[0].LegendMinThreshold, ('On, 0'))
legends_state.legendmaxthreshold = (contour0_legends[0].LegendMaxThreshold, ('"On", 3.8E-4'))

# ------------------------------------------------------------------------------------------------------------------
# Add and modify notes to graphics
# ------------------------------------------------------------------------------------------------------------------

notes_state = dm.NoteState()  # initialize a notes state object for all notes on all graphics, windows, and pages
notes_root = dm.Note(notes_state)  # initialize notes root object for all notes on all graphics, windows, and pages

graphic0_notes = notes_root.add_note(1, window0_graphic0_root)  # default result type is displacement

notes_state.note = (graphic0_notes[0].Root, '"On", "Model Info"')

# ------------------------------------------------------------------------------------------------------------------
# Write session to file
# ------------------------------------------------------------------------------------------------------------------

location1 = 'C:\Users\Yumitomo\OneDrive\Projects\PyPi\dotmvw2github\dotmvw'
name1 = 'test.mvw'
dm.Write(pages_root).mvw(name1, location1)

b = time.time()
print(b - a)