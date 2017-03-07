/*
 * Copyright  2000-2004 The Apache Software Foundation
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 */

package org.apache.tools.ant.taskdefs;

import java.io.File;
import java.io.IOException;
import org.apache.tools.ant.BuildException;
import org.apache.tools.ant.Project;
import org.apache.tools.ant.taskdefs.condition.Os;
import org.apache.tools.ant.types.Commandline;
import org.apache.tools.ant.types.FileSet;
import org.apache.tools.ant.types.PatternSet;

/**
 * Chmod equivalent for unix-like environments.
 *
 * @since Ant 1.1
 *
 * @ant.task category="filesystem"
 * @todo Refactor so it does not extend from ExecuteOn and then turn around
 *       and unsupport several attributes.
 */
public class Chmod extends ExecuteOn {

    private FileSet defaultSet = new FileSet();
    private boolean defaultSetDefined = false;
    private boolean havePerm = false;

    /**
     * Chmod task for setting file and directory permissions.
     */
    public Chmod() {
        super.setExecutable("chmod");
        super.setParallel(true);
        super.setSkipEmptyFilesets(true);
    }

    /**
     * @see org.apache.tools.ant.ProjectComponent#setProject
     */
    public void setProject(Project project) {
        super.setProject(project);
        defaultSet.setProject(project);
    }

    /**
     * The file or single directory of which the permissions must be changed.
     * @param src
     */
    public void setFile(File src) {
        FileSet fs = new FileSet();
        fs.setFile(src);
        addFileset(fs);
    }

    /**
     * The directory which holds the files whose permissions must be changed.
     * @param src
     */
    public void setDir(File src) {
        defaultSet.setDir(src);
    }

    /**
     * The new permissions.
     * @param perm
     */
    public void setPerm(String perm) {
        createArg().setValue(perm);
        havePerm = true;
    }

    /**
     * Add a name entry on the include list.
     */
    public PatternSet.NameEntry createInclude() {
        defaultSetDefined = true;
        return defaultSet.createInclude();
    }

    /**
     * Add a name entry on the exclude list.
     */
    public PatternSet.NameEntry createExclude() {
        defaultSetDefined = true;
        return defaultSet.createExclude();
    }

    /**
     * Add a set of patterns.
     */
    public PatternSet createPatternSet() {
        defaultSetDefined = true;
        return defaultSet.createPatternSet();
    }

    /**
     * Sets the set of include patterns. Patterns may be separated by a comma
     * or a space.
     *
     * @param includes the string containing the include patterns
     */
    public void setIncludes(String includes) {
        defaultSetDefined = true;
        defaultSet.setIncludes(includes);
    }

    /**
     * Sets the set of exclude patterns. Patterns may be separated by a comma
     * or a space.
     *
     * @param excludes the string containing the exclude patterns
     */
    public void setExcludes(String excludes) {
        defaultSetDefined = true;
        defaultSet.setExcludes(excludes);
    }

    /**
     * Sets whether default exclusions should be used or not.
     *
     * @param useDefaultExcludes "true"|"on"|"yes" when default exclusions
     *                           should be used, "false"|"off"|"no" when they
     *                           shouldn't be used.
     */
    public void setDefaultexcludes(boolean useDefaultExcludes) {
        defaultSetDefined = true;
        defaultSet.setDefaultexcludes(useDefaultExcludes);
    }

    protected void checkConfiguration() {
        if (!havePerm) {
            throw new BuildException("Required attribute perm not set in chmod",
                                     getLocation());
        }

        if (defaultSetDefined && defaultSet.getDir(getProject()) != null) {
            addFileset(defaultSet);
        }
        super.checkConfiguration();
    }

    public void execute() throws BuildException {
        /*
         * In Ant 1.1, <chmod dir="foo" /> means, change the permissions
         * of directory foo, not anything inside of it.  This is the case the
         * second branch of the if statement below catches for backwards
         * compatibility.
         */
        if (defaultSetDefined || defaultSet.getDir(getProject()) == null) {
            try {
                super.execute();
            } finally {
                if (defaultSetDefined && defaultSet.getDir(getProject()) != null) {
                    filesets.removeElement(defaultSet);
                }
            }
        } else if (isValidOs()) {
            // we are chmodding the given directory
            Execute execute = prepareExec();
            Commandline cloned = (Commandline) cmdl.clone();
            cloned.createArgument().setValue(defaultSet.getDir(getProject())
                                             .getPath());
            try {
                execute.setCommandline(cloned.getCommandline());
                runExecute(execute);
            } catch (IOException e) {
                throw new BuildException("Execute failed: " + e, e, getLocation());
            } finally {
                // close the output file if required
                logFlush();
            }
        }
    }

    /**
     * @ant.attribute ignore="true"
     */
    public void setExecutable(String e) {
        throw new BuildException(getTaskType()
            + " doesn\'t support the executable attribute", getLocation());
    }

    /**
     * @ant.attribute ignore="true"
     */
    public void setCommand(Commandline cmdl) {
        throw new BuildException(getTaskType()
            + " doesn\'t support the command attribute", getLocation());
    }

    /**
     * @ant.attribute ignore="true"
     */
    public void setSkipEmptyFilesets(boolean skip) {
        throw new BuildException(getTaskType()
            + " doesn\'t support the skipemptyfileset attribute", getLocation());
    }

    /**
     * @ant.attribute ignore="true"
     */
    public void setAddsourcefile(boolean b) {
        throw new BuildException(getTaskType()
            + " doesn\'t support the addsourcefile attribute", getLocation());
    }

    protected boolean isValidOs() {
        return Os.isFamily("unix") && super.isValidOs();
    }
}
