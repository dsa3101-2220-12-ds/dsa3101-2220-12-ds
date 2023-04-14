import org.gephi.graph.api.*;
import org.gephi.io.exporter.api.ExportController;
import org.gephi.io.exporter.preview.JSONExporter;
import org.gephi.io.processor.plugin.DefaultProcessor;
import org.gephi.io.importer.api.Container;
import org.gephi.io.importer.api.ImportController;
import org.gephi.project.api.ProjectController;
import org.gephi.project.api.Workspace;
import org.openide.util.Lookup;

import java.io.File;
import java.io.IOException;

public class ExportGraphToJSON {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java ExportGraphToJSON <input_gexf_file> <output_json_file>");
            System.exit(1);
        }

        String inputFilename = args[0];
        String outputFilename = args[1];

        ProjectController projectController = Lookup.getDefault().lookup(ProjectController.class);
        projectController.newProject();
        Workspace workspace = projectController.getCurrentWorkspace();

        ImportController importController = Lookup.getDefault().lookup(ImportController.class);
        Container container;
        try {
            File file = new File(inputFilename);
            container = importController.importFile(file);
        } catch (Exception ex) {
            System.err.println("Error: Failed to import the GEXF file");
            ex.printStackTrace();
            System.exit(1);
            return;
        }

        importController.process(container, new DefaultProcessor(), workspace);

        ExportController exportController = Lookup.getDefault().lookup(ExportController.class);
        JSONExporter jsonExporter = (JSONExporter) exportController.getExporter("json");
        jsonExporter.setExportVisible(true);

        try {
            exportController.exportFile(new File(outputFilename), jsonExporter);
        } catch (IOException ex) {
            System.err.println("Error: Failed to export the JSON file");
            ex.printStackTrace();
            System.exit(1);
        }

        System.out.println("Graph exported successfully to: " + outputFilename);
    }
}

