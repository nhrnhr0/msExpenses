module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        run: {
            svelte: {
                exec: 'npm run build'
            }
        },
        watch: {
            svelte: {
                files: ['src/**/*.*'],
                tasks: ['run:svelte']
            }
        },
        
    });
    grunt.loadNpmTasks('grunt-run');
    grunt.loadNpmTasks('grunt-contrib-watch');
    //grunt.registerTask('defualt', '')
}